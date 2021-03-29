/*
 * Protocol20W18.h
 *
 *  Created on: 3 May 2020
 *      Author: Arion
 */

#ifndef PROTOCOL_PROTOCOL20W18_H_
#define PROTOCOL_PROTOCOL20W18_H_

#include <cstdint>
#include <chrono>

struct PingPacket {
	std::chrono::time_point<std::chrono::high_resolution_clock, std::chrono::nanoseconds> time = std::chrono::high_resolution_clock::now();
} __attribute__((packed));


struct ConnectPacket {
	uint8_t name[32];
} __attribute__((packed));


struct DisconnectPacket {
	;
} __attribute__((packed));


struct RequestPacket {
	uint16_t uuid;
	uint8_t action_id;
	uint8_t target_id;
	uint32_t payload;
} __attribute__((packed));


struct AcknowledgePacket {
	uint16_t uuid;
	uint8_t result;
} __attribute__((packed));


struct ResponsePacket {
	uint16_t uuid;
	uint8_t action_id;
	uint8_t target_id;
	uint32_t payload;
} __attribute__((packed));


struct ProgressPacket {
	uint32_t uuid;
	uint8_t progress;
} __attribute__((packed));


struct DataPacket {
	uint32_t data;
} __attribute__((packed));


struct MessagePacket {
	uint8_t message[128];
} __attribute__((packed));


struct ErrorPacket {
	uint8_t error_id;
} __attribute__((packed));


#endif /* PROTOCOL_PROTOCOL20W18_H_ */
