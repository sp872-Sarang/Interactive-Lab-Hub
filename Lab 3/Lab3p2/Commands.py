#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
rec = KaldiRecognizer(model, wf.getframerate(), '["left right front back stop", "[unk]"]')

def performAction(word):
        if word == 'left':
            print("Moving left")
        elif word == 'right':
            print("Moving right")
        elif word == 'forward':
            print("Moving forward")
        elif word == 'back':
            print("Moving back")
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
        