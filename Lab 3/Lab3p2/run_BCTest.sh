
arecord -D hw:1,0 -f cd -c1 -r 44100 -d 5 -t wav rec_mono.wav
python Car.py rec_mono.wav
