/*
 * NetworkClientIO.cpp
 *
 *  Created on: 26 Apr 2020
 *      Author: Arion
 */

#include "NetworkClientIO.h"


#ifdef BUILD_WITH_NETWORK_CLIENT_IO


#include <iostream>

#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <thread>
#include <pthread.h>
/*
 * Creates an ExternalIO interface using the given port number.
 * This constructor invocation is a light operation.
 */
NetworkClientIO::NetworkClientIO(const char* address_str, uint16_t port) {
	this->address = { 0 };
	this->socket_id = 0;
	this->connected = false;
	this->receiver = nullptr;
	this->address_str = address_str;

	address.sin_family = AF_INET;
	address.sin_port = htons(port);
}

/*
 * Releases IO resources
 */
NetworkClientIO::~NetworkClientIO() {
	disconnectClient();
}


/*
 * Creates a server socket and allow incoming connections
 * through the port specified by the constructor.
 * This operation is heavy and may fail.
 * Check the returned error code and set breakpoints accordingly if needed.
 */
int8_t NetworkClientIO::connectClient() {
	if(connected) {
		return -1; // Server already connected
	}

	int32_t result;

	// Creates the socket instance
	socket_id = socket(AF_INET, SOCK_STREAM, 0);

	if(socket_id < 0) {
		return -2;
	}


	if(inet_pton(AF_INET, address_str, &address.sin_addr) <= 0) {
		close(socket_id);
		return -3;
	}

	// Binds the client socket to the specified address and port
	result = connect(socket_id, (struct sockaddr*) &address, sizeof(address));

	if(result < 0) {
		close(socket_id);
		return -4;
	}

	// Finalises the instance's state and adds the socket server to the array of opened sockets
	this->connected = true;

	// Creates the reception thread
	this->reception_thread = std::thread(&NetworkClientIO::receiveThread, this);

	return true;
}

/*
 * Disconnects the ExternalIO instance.
 * In particular, this function resets the ExternalIO to an initial state and closes all used IO resources.
 * Make sure the disconnect member function is only called in the reception thread.
 */
void NetworkClientIO::disconnectClient() {
	if(connected) {
		this->connected = false;
		closeSocket();
	}
	this->reception_thread.detach(); // very important to handle disconnections
}

bool NetworkClientIO::is_connected() {
	return connected;
}

/*
 * Closes all used IO resources
 */
void NetworkClientIO::closeSocket() {
	close(socket_id);
}

/*
 * Reception thread
 *
 * Allows incoming connections and adds the corresponding socket to the array of opened sockets.
 * Processes input from the remote connections and passes it to the reception handler.
 * Handles closing connections.
 */
void NetworkClientIO::receiveThread() {
	int32_t result;

	uint8_t buffer[256];

	std::cout << "[Client@" << ntohs(address.sin_port) << "] Client connected" << std::endl;

	while(connected) {
		// New data from client
		while((result = recv(socket_id, buffer, sizeof(buffer), 0)) >= 0) {
			if(result != 0) {
				if(receiver != nullptr) {
					if(ntohs(address.sin_port) == PORT_A) {
						receiver(0b10000000, buffer, result); // Sender ID marked as external
					} else {
						receiver(0b11000000, buffer, result); // Sender ID marked as internal
					}
				}
			} else {
				// Connection was closed by server
				std::cout << "[Client@" << ntohs(address.sin_port) << "] Client disconnected by server" << std::endl;
				disconnectClient();
				break;
				// Do not decrement the num_sockets field since our IDs are not linear
			}
		}
	}

	//std::cout << "[Client@" << ntohs(address.sin_port) << "] Client disconnected" << std::endl;

	// disconnectClient();
	return;
}

/*
 * Sets the receiver callback function
 */
void NetworkClientIO::receive(const std::function<void (uint8_t sender_id, uint8_t* buffer, uint32_t length)> &receiver) {
	this->receiver = receiver;
}

/*
 * Broadcasts data to the array of connected sockets (excluding the server instance)
 */
void NetworkClientIO::transmit(uint8_t* buffer, uint32_t length) {
	if(connected) {
		int32_t result;

		while((result = send(socket_id, buffer, length, 0)) > 0) {
			length -= result;
		}
	}
}

#endif /* BUILD_WITH_NETWORK_CLIENT_IO */
