import time
import board
import busio
import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/your/topic/here'

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    for i in range(12):
        if mpr121[i].value:
<<<<<<< HEAD
            val = f"Twizzler {i} touched!"
            print(val)
            client.publish(topic, val)
=======
        	val = f"Twizzler {i} touched!"
        	print(val)
        	client.publish(topic, val)
>>>>>>> 51b2cc03cc5625007ea31708d6846319c13c103f
    time.sleep(0.25)
