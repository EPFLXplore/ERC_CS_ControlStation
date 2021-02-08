/*
 * NetworkServerIO.h
 *
 *  Created on: 27 Apr 2020
 *      Author: Arion
 */

#ifndef NETWORKSERVERIO_H_
#define NETWORKSERVERIO_H_

#include "Build.h"


#ifdef BUILD_WITH_NETWORK_SERVER_IO


#include "IODriver.h"
#include "NetworkIO.h"

#include <cstdint>
#include <functional>
#include <thread>
#include <pthread.h>

#include <arpa/inet.h>
#include <sys/poll.h>


static const uint32_t MAX_CLIENTS = 64;

class NetworkServerIO : public IODriver {
public:
	NetworkServerIO(uint16_t port);
	~NetworkServerIO();

	int8_t connectServer();
	void disconnectServer();

	void receive(const std::function<void (uint8_t sender_id, uint8_t* buffer, uint32_t length)> &receiver);
	void transmit(uint8_t* buffer, uint32_t length);

private:
	sockaddr_in address;
	bool connected;
	std::thread reception_thread;
	struct pollfd sockets[MAX_CLIENTS];
	uint32_t num_sockets;
	std::function<void (uint8_t sender_id, uint8_t* buffer, uint32_t length)> receiver;

	void receiveThread();
	void closeSockets();
};


#endif /* BUILD_WITH_NETWORK_SERVER_IO */

#endif /* NETWORKSERVERIO_H_ */
