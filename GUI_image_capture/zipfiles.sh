#! /bin/bash

today=`date +%Y-%m-%d:%H:%M:%S`

zip -r "/home/pi/BIOE_521_Final_Project/GUI_image_capture/saved-$today.zip" /home/pi/BIOE_521_Final_Project/GUI_image_capture/saved
