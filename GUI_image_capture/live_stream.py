# USAGE
# python live_stream.py --output output
# Main script to launch Focus Stacking program.

# This was adapted from Adrian
# Rosebrocks blog post on "Displaying a video feed with OpenCV and Tkinter" at
# pyimagesearch.com

# import the necessary packages
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

#Remove old image files in input folder
image_files="/home/pi/BIOE_521_Final_Project/GUI_image_capture/input/*"
r=glob.glob(image_files)
for i in r:
        os.remove(i)

#Remove old image files in saved folder
image_files="/home/pi/BIOE_521_Final_Project/GUI_image_capture/saved/*"
r=glob.glob(image_files)
for i in r:
        os.remove(i)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to output directory to store snapshots")
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warmup
print("[INFO] warming up camera...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

# start the app
pba = LiveStreamApp(vs, args["output"])
pba.root.mainloop()
