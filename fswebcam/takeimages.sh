#! /bin/bash

cd /home/pi/BIOE_521_Final_Project/focusstack/input
rm -f *

cd /home/pi/BIOE_521_Final_Project/fswebcam

counter=1

while [[ $counter -le 10 ]]
do
	./camera.sh;
	sleep 10;
	((counter++))
done
