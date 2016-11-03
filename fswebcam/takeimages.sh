#! /bin/bash

cd /home/pi/BIOE_521_Final_Project/focusstack/input
rm -f *.jpg

cd /home/pi/BIOE_521_Final_Project/fswebcam
while true;do
	./camera.sh;
	sleep 5;
done
