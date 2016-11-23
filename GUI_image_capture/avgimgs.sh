#! /bin/bash

#grabs the current time stamp
today=`date +%Y-%m-%d:%H:%M:%S`

#averages images at step that was just completed
cd output
convert -average *.jpg output.jpg
cp output.jpg "/home/pi/BIOE_521_Final_Project/GUI_image_capture/input/$today.jpg"
cd /home/pi/BIOE_521_Final_Project/GUI_image_capture