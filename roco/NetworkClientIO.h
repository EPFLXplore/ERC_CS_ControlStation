/*
 * NetworkClientIO.h
 *
 *  Created on: 27 Apr 2020
 *      Author: Arion
 */

#ifndef NETWORKCLIENTIO_H_
#define NETWORKCLIENTIO_H_

#include "Build.h"


#ifdef BUILD_WITH_NETWORK_CLIENT_IO


#include "IODriver.h"
#include "NetworkIO.h"

#include <cstdint>
#include <functional>
#include <thread>
#include <arpa/inet.h>
#include <sys/poll.h>
#include <pthread.h>


class NetworkClientIO : public IODriver {
public:
	NetworkClientIO(const char* address, uint16_t port);
	~NetworkClientIO();

	int8_t connectClient();
	void disconnectClient();
	bool is_connected();

	void receive(const std::function<void (uint8_t sender_id, uint8_t* buffer, uint32_t length)> &receiver);
	void transmit(uint8_t* buffer, uint32_t length);


private:
	const char* address_str;
	sockaddr_in address;
	uint32_t socket_id;
	bool connected;
	std::thread reception_thread;
	std::function<void (uint8_t sender_id, uint8_t* buffer, uint32_t length)> receiver;

	void receiveThread();
	void closeSocket();
};


#endif /* BUILD_WITH_NETWORK_CLIENT_IO */

#endif /* NETWORKCLIENTIO_H_ */
