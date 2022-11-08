import paho.mqtt.client as mqtt
import uuid

import time
import board
import busio
import adafruit_mpr121


i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)


from subprocess import call

#func
def speak_command(command):
  #text2speech vars
  cmd_beg= 'echo '
  cmd_end = '| festival --tts'
  Speech_cmd_start = command
  call([cmd_beg+Speech_cmd_start+cmd_end], shell = True)



# the # wildcard means we subscribe to all subtopics of IDD
topic = 'IDD/SecuritySystem_Sp'

# some other examples
# topic = 'IDD/a/fun/topic'

#this is the callback that gets called once we connect to the broker. 
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
	print(f"connected with result code {rc}")
	client.subscribe(topic)
	# you can subsribe to as many topics as you'd like
	# client.subscribe('some/other/topic')


# this is the callback that gets called each time a message is recived
def on_message(cleint, userdata, msg):
    print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    
    Speech_cmd_start = 'There is an Intruder! RUN'
    speak_command(Speech_cmd_start)
    print("User detected")
    # you can filter by topics
    # if msg.topic == 'IDD/some/other/topic': do thing

client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

t = 'IDD/SecuritySystem_Sp_Owner'
client.publish(t,'Owner system online')


# this is blocking. to see other ways of dealing with the loop
#  https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
client.loop_forever()
