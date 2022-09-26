#!/bin/bash

echo "How old are you today?" | festival --tts

arecord -D hw:1,0 -f cd -c1 -r 16000 -d 5 -t wav recorded_mono.wav
