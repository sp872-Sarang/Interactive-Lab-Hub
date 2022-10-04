#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json
import RPi.GPIO as GPIO
import time
# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)
# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse
GPIO.setup(7,GPIO.OUT)
servo2 = GPIO.PWM(7,50) # Note 11 is pin, 50 = 50Hz pulse
#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
servo2.start(0)


if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
rec = KaldiRecognizer(model, wf.getframerate(), '["left right go back stop", "[unk]"]')

def setduty(val):
    servo1.ChangeDutyCycle(val)
    servo2.ChangeDutyCycle(val)

def servoForward():
    dutyLeftW = 1
    dutyRightW = 12
            # Loop for duty values from 2 to 12 (0 to 180 degrees)
    while dutyLeftW <= 12 and dutyRightW >= 1:
        servo1.ChangeDutyCycle(dutyLeftW)
        servo2.ChangeDutyCycle(dutyRightW)
        time.sleep(0.1)
        servo1.ChangeDutyCycle(0)
        servo1.ChangeDutyCycle(0)
        time.sleep(0.1)
        dutyLeftW = dutyLeftW + 1
        dutyRightW = dutyRightW - 1
    
    #setduty(0)

def servoBack():
    dutyLeftW = 12
    dutyRightW = 1
            # Loop for duty values from 2 to 12 (0 to 180 degrees)
    while dutyLeftW >=1 and dutyRightW <= 12:
        servo1.ChangeDutyCycle(dutyLeftW)
        servo2.ChangeDutyCycle(dutyRightW)
        time.sleep(0.1)
        servo1.ChangeDutyCycle(0)
        servo1.ChangeDutyCycle(0)
        time.sleep(0.1)
        dutyLeftW = dutyLeftW - 1
        dutyRightW = dutyRightW + 1

def servoRight(val=12):
    #dutyRightW = 12
    dutyLeftW = 1
            # Loop for duty values from 2 to 12 (0 to 180 degrees)
    while dutyLeftW <= val:
        servo1.ChangeDutyCycle(dutyLeftW)
        #servo2.ChangeDutyCycle(dutyRightW)
        #time.sleep(0.1)
        #servo1.ChangeDutyCycle(0)
        #servo1.ChangeDutyCycle(0)
        time.sleep(0.1)
        dutyLeftW = dutyLeftW + 1

def servoLeft(val=12):
    dutyRightW = val
    
            # Loop for duty values from 2 to 12 (0 to 180 degrees)
    while dutyRightW >= 1:
        #servo1.ChangeDutyCycle(dutyLeftW)
        servo2.ChangeDutyCycle(dutyRightW)
        #time.sleep(0.1)
        #servo1.ChangeDutyCycle(0)
        #servo1.ChangeDutyCycle(0)
        time.sleep(0.1)
        dutyRightW = dutyRightW - 1
        #dutyLeftW = dutyLeftW + 2
    

def performAction(word):
        if word == 'left':
            print("Moving left")
            servoLeft()
            
        elif word == 'right':
            print("Moving right")
            servoRight()
            
        elif word == 'go':
            print("Moving forward")
            servoForward()
            
                
        elif word == 'back':
            print("Moving back")
            servoBack()
            
        elif word == 'stop':
            print("Coming to a Halt")

def ActuatorAction(rec):
    
    #print("Result : ",rec.Result())
    #temp = rec.Result()
    #print(type(temp))
    res = json.loads(rec.Result())
    
    print("JSON : ",res)
    ReceivedText = res["text"]
    print(ReceivedText)

    phrase_list = [w for w in ReceivedText.split(' ')]

    print(phrase_list)
    
    for phrase in phrase_list:
        performAction(phrase)


while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        
        ActuatorAction(rec)
        




        




