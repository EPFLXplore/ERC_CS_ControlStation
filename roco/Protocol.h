/*
 * Protocol.h
 *
 *  Created on: 12 Feb 2020
 *      Author: Arion
 */

#ifndef PROTOCOL_PROTOCOL_H_
#define PROTOCOL_PROTOCOL_H_

#include "Build.h"


#ifdef PROTOCOL_20W18
#include "Protocol20W18.h"
#endif /* PROTOCOL_20W18 */

#ifdef PROTOCOL_21W3
#include "Protocol21W3.h"
#endif /* PROTOCOL_20W18 */


#endif /* PROTOCOL_PROTOCOL_H_ */
