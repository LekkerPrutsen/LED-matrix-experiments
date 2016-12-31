# -*- coding: utf-8 -*-

import time
from random import randint
import max7219.led as led

device = led.matrix(cascaded=4)

device.orientation(90)

print "Press Ctrl+C to stop"

#ASCII codes 
symbol01 = 219
symbol02 = 240
symbol03 = 45
symbol04 = 32

duration = 0.2

try: 
    while True:
        #position 1
        device.letter(0, symbol01)
        device.letter(1, symbol02)
        device.letter(2, symbol04)
        device.letter(3, symbol04)
        time.sleep(duration)

        #position 2
        device.letter(0, symbol02)
        device.letter(1, symbol01)
        device.letter(2, symbol04)
        device.clear(3)
        time.sleep(duration)

        #position 3
        device.letter(0, symbol03)
        device.letter(1, symbol02)
        device.letter(2, symbol01)
        device.clear(3)
        time.sleep(duration)

        #position 4
        device.letter(0, symbol04)
        device.letter(1, symbol03)
        device.letter(2, symbol02)
        device.letter(3, symbol01)
        time.sleep(duration)

        #position 5
        device.clear(0)
        device.letter(1, symbol04)
        device.letter(2, symbol01)
        device.letter(3, symbol02)
        time.sleep(duration)
        
        #position 6
        device.clear(0)
        device.letter(1, symbol01)
        device.letter(2, symbol02)
        device.letter(3, symbol03)
        time.sleep(duration) 

 
except KeyboardInterrupt:
    device.clear()
  
    
    
    






