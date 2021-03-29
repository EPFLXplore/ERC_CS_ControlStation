/*
 * NetworkServerIO.cpp
 *
 *  Created on: 26 Apr 2020
 *      Author: Arion
 */

#include "NetworkServerIO.h"


#ifdef BUILD_WITH_NETWORK_SERVER_IO


#include <iostream>
#include <cstring>

#include <sys/socket.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <pthread.h>

/*
 * Creates an ExternalIO interface using the given port number.
 * This constructor invocation is a light operation.
 */
NetworkServerIO::NetworkServerIO(uint16_t port) {
	this->address = { 0 };
	this->connected = false;
	this->num_sockets = 0;
	this->receiver = nullptr;
	memset(sockets, 0, sizeof(sockets));

	address.sin_family = AF_INET;
	address.sin_addr.s_addr = INADDR_ANY;
	address.sin_port = htons(port);
}

/*
 * Releases IO resources
 */
NetworkServerIO::~NetworkServerIO() {
	disconnectServer();
}

/*
 * Creates a server socket and allow incoming connections
 * through the port specified by the constructor.
 * This operation is heavy and may fail.
 * Check the returned error code and set breakpoints accordingly if needed.
 */
int8_t NetworkServerIO::connectServer() {
	if(connected) {
		return -1; // Server already connected
	}

	int32_t result;
	uint32_t enabled = 1;

	// Creates the socket instance
	uint32_t server_socket_id = socket(AF_INET, SOCK_STREAM, 0);

	if(server_socket_id < 0) {
		return -2;
	}

	// Allows socket to reuse address even if the process terminates abruptly
	result = setsockopt(server_socket_id, SOL_SOCKET, SO_REUSEADDR, (uint8_t*) &enabled, sizeof(enabled));

	if(result < 0) {
		close(server_socket_id);
		return -3;
	}


	// Sets the server socket as non-blocking to allow the poll operation to function properly
	result = ioctl(server_socket_id, FIONBIO, (uint8_t*) &enabled);

	if(result < 0) {
		close(server_socket_id);
		return -4;
	}

	// Binds the server socket to the specified port (and address)
	result = bind(server_socket_id, (struct sockaddr*) &address, sizeof(address));

	if(result < 0) {
		close(server_socket_id);
		return -5;
	}

	// Allows incoming connections with a maximal number of pending connections of 16
	result = listen(server_socket_id, 16);

	if(result < 0) {
		close(server_socket_id);
		return -5;
	}


	// Finalises the instance's state and adds the socket server to the array of opened sockets
	this->connected = true;

	sockets[0].fd = server_socket_id;
	sockets[0].events = POLLIN;
	num_sockets++;

	// Creates the reception thread
	this->reception_thread = std::thread(&NetworkServerIO::receiveThread, this);

	return true;
}

/*
 * Disconnects the ExternalIO instance.
 * In particular, this function resets the ExternalIO to an initial state and closes all used IO resources.
 * Make sure the disconnect member function is only called in the reception thread.
 */
void NetworkServerIO::disconnectServer() {
	if(connected) {
		this->connected = false;
		closeSockets();
	}
}

/*
 * Closes all used IO resources
 */
void NetworkServerIO::closeSockets() {
	for(uint32_t i = 0; i < num_sockets; i++) {
		uint32_t fd = sockets[i].fd;

		if(fd >= 0) {
			close(fd);
		}
	}

	this->num_sockets = 0;
	memset(sockets, 0, sizeof(sockets));
}

/*
 * Reception thread
 *
 * Allows incoming connections and adds the corresponding socket to the array of opened sockets.
 * Processes input from the remote connections and passes it to the reception handler.
 * Handles closing connections.
 */
void NetworkServerIO::receiveThread() {
	int32_t result;

	uint8_t buffer[256];

	std::cout << "[Server@" << ntohs(address.sin_port) << "] Server started" << std::endl;

	while(connected) {
		result = poll(sockets, num_sockets, -1);

		if(result < 0) {
			std::cout << "[Server@" << ntohs(address.sin_port) << "] Poll failed" << std::endl;
			break;
		}

		for(uint32_t i = 0; i < num_sockets; i++) {
			uint32_t socket_id = sockets[i].fd;

			if(sockets[i].revents == 0) {
				continue; // Nothing new on this socket
			}

			if(i == 0) { // New connection
				uint32_t new_socket;

				while((new_socket = accept(socket_id, nullptr, nullptr)) != -1) {
					std::cout << "[Server@" << ntohs(address.sin_port) << "] Client connected (ID " << num_sockets << ")" << std::endl;

					sockets[num_sockets].fd = new_socket;
					sockets[num_sockets].events = POLLIN;

					num_sockets++;
				}
			} else { // New data from client
				while((result = recv(socket_id, buffer, sizeof(buffer), 0)) >= 0) {
					if(result != 0) {
						if(receiver != nullptr) {
							if(ntohs(address.sin_port) == PORT_A) {
								receiver(0b10000000 | i, buffer, result); // Sender ID marked as external
							} else {
								receiver(0b11000000 | i, buffer, result); // Sender ID marked as internal
							}
						}
					} else {
						// Connection was closed by client
						std::cout << "[Server@" << ntohs(address.sin_port) << "] Client disconnected (ID " << i << ")" << std::endl;
						close(socket_id);
						sockets[i].fd = -1;
						// Do not decrement the num_sockets field since our IDs are not linear
					}
				}
			}
		}
	}

	std::cout << "[Server@" << ntohs(address.sin_port) << "] Server stopped" << std::endl;

	closeSockets();
}

/*
 * Sets the receiver callback function
 */
void NetworkServerIO::receive(const std::function<void (uint8_t sender_id, uint8_t* buffer, uint32_t length)> &receiver) {
	this->receiver = receiver;
}

/*
 * Broadcasts data to the array of connected sockets (excluding the server instance)
 */
void NetworkServerIO::transmit(uint8_t* buffer, uint32_t length) { // Broadcast
	int32_t result;
	uint32_t remaining;

	for(uint32_t i = 1; i < num_sockets; i++) {
		uint32_t socket_id = sockets[i].fd;
		remaining = length;

		while((result = send(socket_id, buffer, remaining, 0)) > 0) {
			remaining -= result;
		}
	}
}

#endif /* BUILD_WITH_NETWORK_SERVER_IO */
