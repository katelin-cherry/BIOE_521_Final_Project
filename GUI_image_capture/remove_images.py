from __future__ import print_function
from livestreamapp import LiveStreamApp
from imutils.video import VideoStream
import argparse
import time
import glob,os


#Remove old image files in output folder
image_files="/home/pi/BIOE_521_Final_Project/GUI_image_capture/output/*"
r=glob.glob(image_files)
for i in r:
        os.remove(i)
