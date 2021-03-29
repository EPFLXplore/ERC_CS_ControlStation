/*
 * NetworkBus.cpp
 *
 *  Created on: 8 May 2020
 *      Author: Arion
 */

#include "Build/Build.h"


#ifdef BUILD_WITH_NETWORK_BUS


#include "NetworkBus.h"
#include "Protocol/Protocol.h"

NetworkBus::NetworkBus(IODriver* driver) : IOBus(driver, network_frame, sizeof(network_frame)) {

	define<Avionics_BaroTempPacket>(0);
	define<Avionics_AccelMagPacket>(1);
	define<Handling_GripperPacket>(2);
	define<Power_SystemPacket>(3);
	define<Power_VoltagePacket>(4);
	define<Power_CurrentPacket>(5);
	define<Science_MeasurePacket>(6);

	define<DataPacket>(7);

	define<PingPacket>(59);
	define<RequestPacket>(60);
	define<ResponsePacket>(61);
	define<ProgressPacket>(62);
	define<ErrorPacket>(63);
}


#endif /* BUILD_WITH_NETWORK_BUS */
