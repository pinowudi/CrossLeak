#!/bin/bash

pkill wifi_scanner.py
pkill pimotion.py
pkill piaudio.py

while true; do
	echo "start"
#	./wifi_scanner.py &
#	export scanner_pid=$!
	./pimotion.py &
	export camera_pid=$!
#	./piaudio.py > /dev/null 2>&1 &
	./piaudio.py &
	export audio_pid=$!

	sleep 60
#	kill $scanner_pid
	kill $camera_pid
	kill $audio_pid
	echo "time up"

	./renaming.py
	./file_transfer.py

done
