/*
 * Protocol.h
 *
 *  Created on: 12 Feb 2020
 *      Author: Arion
 */

#ifndef PROTOCOL_PROTOCOL_H_
#define PROTOCOL_PROTOCOL_H_

#define BUILD_FOR_TESTING

#include "../Build/Build.h"


//#ifdef PROTOCOL_20W18
//#include "Protocol20W18.h"

#ifdef PROTOCOL_21W3
#include "Protocol21W3.h"

#endif /* PROTOCOL_21W3 */


#endif /* PROTOCOL_PROTOCOL_H_ */
