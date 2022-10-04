
arecord -D hw:3,0 -f cd -c1 -r 16000 -d 5 -t wav rec_mono.wav
python3 Commands.py rec_mono.wav
