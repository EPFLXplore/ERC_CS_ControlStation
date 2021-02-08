/*
 * ProtocolRegisters.h
 *
 *  Created on: 8 May 2020
 *      Author: Arion
 */

#ifndef PROTOCOL_PROTOCOLREGISTERS_H_
#define PROTOCOL_PROTOCOLREGISTERS_H_

// This file may only be included by MessageBus.cpp (which exports the REGISTER macro)
#include "Protocol.h"

#ifdef PROTOCOL_20W18
REGISTER(PingPacket)
REGISTER(ConnectPacket)
REGISTER(DisconnectPacket)
REGISTER(RequestPacket)
REGISTER(AcknowledgePacket)
REGISTER(ResponsePacket)
REGISTER(ProgressPacket)
REGISTER(DataPacket)
REGISTER(MessagePacket)
REGISTER(ErrorPacket)
#endif /* PROTOCOL_20W18 */

#ifdef PROTOCOL_21W3
REGISTER(PingPacket)
REGISTER(RequestPacket)
REGISTER(ResponsePacket)
REGISTER(ProgressPacket)
REGISTER(ErrorPacket)

REGISTER(DataPacket)

REGISTER(Avionics_BaroTempPacket)
REGISTER(Avionics_AccelMagPacket)
REGISTER(Handling_GripperPacket)
REGISTER(Power_SystemPacket)
REGISTER(Power_VoltagePacket)
REGISTER(Power_CurrentPacket)
REGISTER(Science_MeasurePacket)
#endif


#endif /* PROTOCOL_PROTOCOLREGISTERS_H_ */
