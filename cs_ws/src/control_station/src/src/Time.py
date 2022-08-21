#
# @file: Time.py
# 
# @date: 20/08/2022
#
# @authors: Emile Hreich
#           emile.janhodithreich@epfl.ch
#
# @brief: 
#-------------------------------------------------------------------------------

# ==============================================================================
# Libraries

import asyncio
import json
import websocket
import time
from threading import Thread

# ==============================================================================

TIME_WS_URL = 'ws://127.0.0.1:8000/ws/CS2022/time/'



class Timer:
    ws = websocket.WebSocket()
    def __init__(self):

        self._seconds = 0
        self._minutes = 0
        self._hours   = 0

        # connect to websocket
        
        
        print("timer created")


    
    def elapse(self):

        while True:
            # update time
            self._seconds += 1
            if (self._seconds > 60):
                self._seconds = 0
                self._minutes += 1
            if (self._minutes > 60):
                self._minutes = 0
                self._hours += 1

            # dump in websocket
            time.sleep(1)

            TimeDictionary = {
            'sec'        : self._seconds, 
            'min'        : self._minutes, 
            'hor'        : self._hours
            
            }

        
            message = json.dumps(TimeDictionary)

            if Timer.ws.connected :
                Timer.ws.send('%s' % message)





def startTimer():

    timer = Timer()
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # try:
    #     # loop.run_until_complete(main())
    #     loop.call_soon_threadsafe(timer.elapse())
    # finally:
    #     loop.run_until_complete(loop.shutdown_asyncgens())
    #     loop.close()
    timer.elapse()

def startThread():
    Timer.ws.connect(TIME_WS_URL)
    thread = Thread(target=startTimer)
    thread.start()