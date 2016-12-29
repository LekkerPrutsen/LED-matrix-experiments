import time
import max7219.led as led

device = led.matrix(cascaded=4)

device.letter(0, ord('1'))
time.sleep(1)
device.clear()

device.letter(1, ord('2'))
time.sleep(1)
device.clear()

device.letter(2, ord('3'))
time.sleep(1)
device.clear()

device.letter(3, ord('4'))
time.sleep(1)
device.clear()






