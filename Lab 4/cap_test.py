import time
import board
import busio
import qwiic_button

import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)
my_button = qwiic_button.QwiicButton()


while True:
    for i in range(12):
        if mpr121[i].value:
                print(f"Twizzler {i} touched!")

    if my_button.is_button_pressed() == True:
            print("\nThe button is pressed!")

    #else:
    #    print("\nThe button is not pressed!")

    time.sleep(0.02)




