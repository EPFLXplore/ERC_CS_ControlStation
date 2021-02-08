/*
 * NetworkBus.h
 *
 *  Created on: 8 May 2020
 *      Author: Arion
 */

#ifndef NETWORKBUS_H_
#define NETWORKBUS_H_

#include "Build.h"


#ifdef BUILD_WITH_NETWORK_BUS


#include "IOBus.h"

#define NETWORK_FRAME_SIZE 256


class NetworkBus : public IOBus {
public:
	NetworkBus(IODriver* driver); // Constructor is inherited

private:
	uint8_t network_frame[NETWORK_FRAME_SIZE];
};


#endif /* BUILD_WITH_NETWORK_BUS */

#endif /* NETWORKBUS_H_ */
