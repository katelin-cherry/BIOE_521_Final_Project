#! /bin/sh

# script that is called in file (~/.config/lxsession/LXDE-pi/autostart) when starting raspberry pi
# This allows the Focus Stacking program to be loaded on startup
cd /
cd home/pi/BIOE_521_Final_Project/GUI_image_capture

# Calls the python script to run python command to start program. Unsuccessful to directly start program through this shell script. 
# Had to work around by calling the following python script which then calls the program. A little bulky but it works!

sudo python launchscript.py 
exit 0
cd /

