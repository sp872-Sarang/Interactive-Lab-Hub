import time
import board
import busio

import adafruit_mpr121
from subprocess import Popen, call


i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    for i in range(12):
        if i == 6 and mpr121[i].value:
            print("This is a bell paper!")
            call(f"espeak 'bell pepper'", shell=True)
            # espeak -ven+f2 -k5 -s150 --stdout  "bell pepper" | aplay
        if i == 10 and mpr121[i].value:
            print("This is an organge!")
            call(f"espeak 'orange'", shell=True)

        # if mpr121[i].value:
        #     print(f"Banana {i} touched!")
    time.sleep(0.25)  # Small delay to keep from spamming output messages.