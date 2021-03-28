/*
 * MessageBus.cpp
 *
 *  Created on: 10 Dec 2019
 *      Author: Arion
 */

/*
 * Dynamic allocation should be avoided. If needed, use pvPortMalloc and pvPortFree instead of new and delete respectively.
 */

#include "MessageBus.h"


// Template explicit instantiation
#define REGISTER(P) 												\
	template bool MessageBus::define<P>(uint8_t);					\
	template bool MessageBus::handle<P>(void (*)(uint8_t, P*, void*), void*);		\
	template bool MessageBus::forward<P>(MessageBus*);				\
	template bool MessageBus::send<P>(P*);


#include "ProtocolRegisters.h"

#undef REGISTER


/*
 * Packet definitions
 *
 * Explicit template instantiation is needed.
 */

/*
 * Registers a message identifier for the specified structure/class.
 *
 * Allows I/O communication for the given message ID according to the bus specification.
 * Using std::typeindex allows more flexibility insofar as the message ID is directly inferred
 * using the template of send_packet.
 *
 * The two first bits of the identifier are used for storing dispatching metadata.
 *
 * Warning: this method is not thread-safe.
 */
template<typename T> bool MessageBus::define(uint8_t identifier) {
	std::size_t struct_size = sizeof(T);

	std::type_index type = std::type_index(typeid(T));
	uint32_t insertion_point = type.hash_code() % 256;

	if(definitions_by_id[identifier & 0b00111111].type != null_type) {
		return false; // Packet ID already in use
	}

	if(struct_size > max_packet_size) {
		return false; // Packet size too large
	}

	while(definitions_by_type[insertion_point] != nullptr) {
		if(definitions_by_type[insertion_point]->type == type) {
			return false; // Packet type already defined
		}

		insertion_point++;

		if(insertion_point == 256) {
			insertion_point = 0;
		}
	}

	PacketDefinition* def = &definitions_by_id[identifier & 0b00111111];

	def->id = identifier;
	def->size = (uint8_t) struct_size;
	def->type = type;

	definitions_by_type[insertion_point] = def;

	return true;
}


/*
 * Registers a handler for this event bus.
 *
 * Accepts a function reference as message handler.
 *
 * Warning: this method is not thread-safe.
 */
template<typename T> bool MessageBus::handle(void (*handler)(uint8_t, T*, void*), void* publisher) {
	std::type_index type = std::type_index(typeid(T));

	PacketDefinition* def = retrieve(type);

	if(def != nullptr) {
		uint8_t packetID = def->id;

		if(handlers[packetID] != nullptr) {
			return false; // A handler is already registered for this packet type
		}

		handlers[packetID] = (void (*)(uint8_t, void*, void*)) handler;
		publishers[packetID] = publisher;

		return true;
	}

	return false;
}


/*
 * Registers a forwarder for this event bus.
 *
 * Every time a packet matching to given type is received, forwards it to the other message bus.
 *
 * Warning: this method is not thread-safe.
 */
template<typename T> bool MessageBus::forward(MessageBus* bus) {
	std::type_index type = std::type_index(typeid(T));

	PacketDefinition* def = retrieve(type);

	if(def != nullptr) {
		uint8_t packetID = def->id;

		if(forwarders[packetID] != nullptr) {
			return false; // A handler is already registered for this packet type
		}

		forwarders[packetID] = bus;

		return true;
	}

	return false;
}

/*
 * Sends the given message using the implemented transmission protocol.
 */
template<typename T> bool MessageBus::send(T *message) {
	std::type_index type = std::type_index(typeid(T));

	PacketDefinition* def = retrieve(type);

	return send(def, (uint8_t*) message);
}

bool MessageBus::send(PacketDefinition* def, uint8_t* data) {
	if(def != nullptr) {
		uint32_t data_bytes_written = 0;

		while(data_bytes_written < def->size) {
			append(&def->id, 1); // Write the packet ID for each transmission frame.
							     // This is only to facilitate the packet reconstruction and should not increment data_bytes_written.

			uint32_t new_bytes = append(data + data_bytes_written, def->size - data_bytes_written); // Send the data

			if(new_bytes == 0) {
				return false;
			} else {
				transmit();
				data_bytes_written += new_bytes;
			}
		}

		return true;
	}

	return false;
}

/*
 * Handles the reception of a message.
 *
 * Provided an external thread calls this method with a buffer to the next incoming message,
 * dispatches the message to the appropriate message handlers.
 */
void MessageBus::receive(uint8_t sender_id, uint8_t *pointer, uint32_t length) {
	if(length > 0) {
		// Safe-cast verification
		uint8_t packet_id = *pointer++;

		PacketDefinition* def = &definitions_by_id[packet_id & 0b00111111];
		ReconstructionBuffer* indexable_buffer = &reconstruction_buffers[sender_id & 0b00111111];

		if(indexable_buffer->index + length > max_packet_size) {
			indexable_buffer->index = 0; // Corrupted packet
			return;
		}

		for(uint16_t i = 0; i < length - 1; i++) {
			indexable_buffer->buffer[indexable_buffer->index++] = *pointer++;
		}

		if(indexable_buffer->index >= def->size) {
			// Packet is complete. Forward buffer to handler.

			if(handlers[packet_id & 0b00111111] != nullptr) {
				handlers[packet_id & 0b00111111](sender_id, indexable_buffer->buffer, publishers[packet_id & 0b00111111]);
			}

			if(forwarders[packet_id & 0b00111111] != nullptr) {
				forwarders[packet_id & 0b00111111]->send(def, indexable_buffer->buffer);
			}

			indexable_buffer->index = 0;
		}
	}
}

/*
 * Searches a packet definition matching the given type in the hash table.
 */
PacketDefinition* MessageBus::retrieve(std::type_index type) {
	uint32_t searchPoint = type.hash_code() % 256;
	uint32_t searchStart = searchPoint;

	while(definitions_by_type[searchPoint] != nullptr) {
		if(definitions_by_type[searchPoint]->type == type) {
			return definitions_by_type[searchPoint];
		}

		searchPoint++;

		if(searchPoint == 256) {
			searchPoint = 0;
		}

		if(searchStart == searchPoint) {
			break; // No packet definition matching the given template type
		}
	}

	return nullptr;
}
