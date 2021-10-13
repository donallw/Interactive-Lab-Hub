#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)

#!/bin/bash
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
#say $*
say "It appears that nobody is home. We will record a message and snap a photo after the beep."

sleep 1[s]

say "BEEP"

#arecord -f cd -r 16000 -d 5 -t wav recorded.wav && sox recorded.wav recorded_mono.wav remix 1,2
numRecordings=$(ls recordings | wc -l)
arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recordings/"guest_recording$numRecordings.wav"

say "Taking photo now"

numPhotos=$(ls photos | wc -l)

ffmpeg -f v4l2 -video_size 1280x720 -i /dev/video0 -frames 1 photos/"guest$numPhotos.jpg"

say "Thank you! Message and photo saved. Have a good day."

./start_wizard.sh
