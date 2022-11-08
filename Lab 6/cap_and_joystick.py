import time
import board
import busio
import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid

import smbus, time
bus = smbus.SMBus(1)
addr = 0x20

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/sp'
topic_joystick = 'IDD/sp_JS'
client.publish(topic,'begin stream')

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    for i in range(12):
        if mpr121[i].value:
            val = f"Twizzler {i} touched!"
            print(val)
            client.publish(topic, val)
            
    bus_data = bus.read_i2c_block_data(addr, 0x03, 5)
    X = (bus_data[0]<<8 | bus_data[1])>>6
    Y = (bus_data[2]<<8 | bus_data[3])>>6
    print(X, Y)
    
    client.publish(topic_joystick, X)
                
    time.sleep(0.25)
    

