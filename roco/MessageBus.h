/*
 * MessageBus.h
 *
 *  Created on: 09 Feb 2020
 *      Author: Arion
 */

#ifndef MESSAGE_BUS_H_
#define MESSAGE_BUS_H_

#include <cstdint>
#include <typeindex>
#include <functional>


static const std::type_index null_type = std::type_index(typeid(nullptr));


struct PacketDefinition {
	uint8_t id;
	uint8_t size;
	std::type_index type = null_type;
};

class MessageBus {
public:
	virtual ~MessageBus() {}

	template<typename T> bool define(uint8_t identifier);
	template<typename T> bool handle(void (*handler)(uint8_t source, T*, void*), void*);
	template<typename T> bool forward(MessageBus* bus);
	template<typename T> bool send(T *message);


protected:
	void receive(uint8_t senderID, uint8_t *pointer, uint32_t length);
	virtual uint8_t append(uint8_t* buffer, uint32_t length) = 0; // Must be atomic
	virtual void transmit() = 0;

private:
	static const uint32_t max_packet_size = 255;
	static const uint32_t max_unique_senders = 64;

	struct ReconstructionBuffer {
		uint8_t buffer[max_packet_size];
		uint8_t index;
	};

	PacketDefinition definitions_by_id[64];
	PacketDefinition* definitions_by_type[256]; // Factor 4 to mitigate hash collisions
	ReconstructionBuffer reconstruction_buffers[max_unique_senders];

	void (*handlers[64])(uint8_t, void*, void*);
	void* publishers[64];
	MessageBus* forwarders[64];

	bool send(PacketDefinition* def, uint8_t* data);
	PacketDefinition* retrieve(std::type_index type);
};


#endif /* MESSAGE_BUS_H_ */
