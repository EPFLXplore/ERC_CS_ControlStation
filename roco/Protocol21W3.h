/*
 * Protocol20W18.h
 *
 *  Created on: 3 May 2020
 *      Author: Arion
 */

#ifndef PROTOCOL_PROTOCOL21W3_H_
#define PROTOCOL_PROTOCOL21W3_H_

#include <cstdint>
#include <chrono>

// General packets
struct PingPacket {
	std::chrono::time_point<std::chrono::high_resolution_clock, std::chrono::nanoseconds> time = std::chrono::high_resolution_clock::now();
} __attribute__((packed));

struct RequestPacket {
	uint16_t uuid;
	uint8_t action_id;
	uint8_t target_id;
	uint32_t payload;
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

struct ErrorPacket {
	uint8_t error_id;
} __attribute__((packed));

// Avionics
struct Avionics_BaroTempPacket {
  float pressure;
  float temperature;
} __attribute__((packed));

struct Avionics_AccelMagPacket {
  float acceleration[3];
  float angular[3];
  float magneto[3];
} __attribute__((packed));

// Handling device
struct Handling_GripperPacket {
  float voltage;
} __attribute__((packed));

// Power
struct Power_VoltagePacket {
  float voltages[4];
} __attribute__((packed));

struct Power_CurrentPacket {
  float currents[4];
} __attribute__((packed));

struct Power_SystemPacket {
  float battery_charge;
  uint8_t state;
} __attribute__((packed));

// Science
struct Science_MeasurePacket {
  float mass;
} __attribute__((packed));

struct DataPacket {
	uint32_t data;
} __attribute__((packed));


#endif /* PROTOCOL_PROTOCOL20W18_H_ */
