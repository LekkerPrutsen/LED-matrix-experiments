# -*- coding: utf-8 -*-

import time
from random import randint
import max7219.led as led

device = led.matrix(cascaded=4)

device.orientation(90)

print "Press Ctrl+C to stop"


try: 
    while True:
        i = randint(0,3)
        
        if i==0:
            j=49
        elif i==1:
            j=50
        elif i==2:
            j=51
        elif i==3:
            j=52

        device.letter(i, j) 
        time.sleep(1)
        device.clear()
 
except KeyboardInterrupt:
    device.clear()
  
    
    
    






