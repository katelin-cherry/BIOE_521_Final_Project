# Script that is called from live_stream.py program.
# It sets up the GUI and calls functions to run program.

# import the necessary packages
from __future__ import print_function
from PIL import Image
from PIL import ImageTk
import Tkinter as tki
import threading
import datetime
import imutils
import cv2
import os
import subprocess

class LiveStreamApp:
	def __init__(self, vs, outputPath):
		# store the video stream object and output path, then initialize
		# the most recently read frame, thread for reading frames, and
		# the thread stop event
		self.vs = vs
		self.outputPath = outputPath
		#self.frame = None
		self.thread = None
		self.stopEvent = None
		self.count=1
		self.steps=1

		# initialize the root window and image panel
		self.root = tki.Tk()
		self.panel = None
		self.root.configure(bg="black")
                #top=Toplevel(self.root)
                #f = Frame(self.root)

		# header
                header_label = tki.Label(self.root, text=" ", bg="black")
                header_label.pack(side="top", expand="no", padx=5, pady=0)
 	        header_label = tki.Label(self.root, text="Low-Cost Focus Stacking", font=("Arial Black",20,"bold"), fg="LightSteelBlue1", bg="black")
 	        header_label.pack(side="top", expand="no", padx=5, pady=0)
 	        header_label = tki.Label(self.root, text="Created by Katelin Cherry & Melody Tan", font=("Arial Black",14,"bold"), fg="LightSteelBlue1", bg="black")
 	        header_label.pack(side="top", expand="no", padx=5, pady=5)
		
 		# user input for time per step (s)
 		self.time_entry = tki.Entry(self.root)
 		self.time_entry.pack(side="bottom", expand="no", padx=5, pady=5)
 		time_label = tki.Label(self.root, text="Time per Step", font=("Arial Black",10,"bold"), fg="LightSteelBlue1", bg="black")
 	        time_label.pack(side="bottom", expand="no", padx=5, pady=0)

 		# user input for number of steps
 	        self.steps_entry = tki.Entry(self.root)
                self.steps_entry.pack(side="bottom", expand="no", padx=5, pady=5)
		steps_label = tki.Label(self.root, text="Number of Steps", font=("Arial Black",10,"bold"), fg="LightSteelBlue1", bg="black")
 		steps_label.pack(side="bottom", expand="no", padx=5, pady=0)

                # Focus Stack Images button - when pressed will focus stack the set of images
 	        # and output the merged image to a window
		FocusStackBtn = tki.Button(self.root, text="Focus Stack Images",
                font=("Arial Black",10,"bold"), bg="LightSteelBlue1", command=self.focusstack)
		FocusStackBtn.pack(side="right", expand="no", padx=5, pady=5)

                # Start Timelapse button
 	        TimelapseBtn = tki.Button(self.root, text="Start Timelapse",
		font=("Arial Black",10,"bold"), bg="LightSteelBlue1", command=self.takeTimelapseMaster)
		TimelapseBtn.pack(side="right", expand="no", padx=5, pady=5)

		# Take Single Image button
		SingleImageBtn = tki.Button(self.root, text="Take Single Image",
		font=("Arial Black",10,"bold"), bg="LightSteelBlue1", command=self.takeSingleImage)
		SingleImageBtn.pack(side="right", expand="no", padx=5, pady=5)

		# start a thread that constantly pools the video sensor for
		# the most recently read frame
		self.stopEvent = threading.Event()
		self.thread = threading.Thread(target=self.videoLoop, args=())
		self.thread.start()

		# set a callback to handle when the window is closed
		self.root.wm_title("FocusStacking Program")
		self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)


	def videoLoop(self):
		# try/except statement is a way to get around
		# a RunTime error that Tkinter throws due to threading
		try:
			# keep looping over frames until we are instructed to stop
			while not self.stopEvent.is_set():
				# grab the frame from the video stream and resize it to
				# have a maximum width of XXX pixels
				self.frame = self.vs.read()
				self.frame = imutils.resize(self.frame, width=500)
				#self.frame.grid(row=10, column=10, padx=10, pady=10)
		
				# OpenCV represents images in BGR order; however PIL
				# represents images in RGB order, so we need to swap
				# the channels, then convert to PIL and ImageTk format
				image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
				image = Image.fromarray(image)
				image = ImageTk.PhotoImage(image)
		
				# if the panel is not None, we need to initialize it
				if self.panel is None:
					self.panel = tki.Label(image=image)
					self.panel.image = image
					self.panel.pack(side="left", padx=10, pady=10)
		
				# otherwise, simply update the panel
				else:
					self.panel.configure(image=image)
					self.panel.image = image

		except RuntimeError, e:
			print("[INFO] caught a RuntimeError")


	# function that will perform the focusstacking when FocusStackButton is clicked
        def focusstack(self):
                # resets counters
                self.count=1
                self.steps=1

                # zips raw images taken during timelapse(currently not working)
                # self.root.after(1,self.ziprawimages)

                # runs focusstacking code
                os.system('python main.py')
                # loads merged focus stacked image in new window
                os.system('python load_image.py --image merged.png')

                          
	# function that takes timelapse of images when TimelapseBtn is clicked
        def takeTimelapseMaster(self):
                # resets count for images taken at each step
                self.count=1
                # takes user input for Number of Steps
                numSteps = int(self.steps_entry.get())
                # takes user input for Time Per Step
		timePerStep = int(self.time_entry.get())
		msPerStep = int(timePerStep*1000)
		# calls function to take multiple images at step
		self.root.after(1, self.takeTimelapse)
		# calls function to average images at step
		self.root.after(2000, self.averageimages)
		# loops through function until number of steps is equal to user's input
		if (self.steps<numSteps):
                        self.steps+=1
                        self.root.after(msPerStep, self.takeTimelapseMaster)

        # function to take multiple images at step
	def takeTimelapse(self):
                if (self.count<= 1):
                        # grab the current timestamp and use it to construct the output path
                        ts = datetime.datetime.now()
                        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S.%f"))
                        # filename = "{}.jpg".format([self.step]+["-"]+[self.count])
                        p = os.path.sep.join((self.outputPath, filename,))
                        self.count+=1
                        # save the file
                        cv2.imwrite(p, self.frame.copy())
                        print("[INFO] saved {}".format(filename))
                        self.root.after(10, self.takeTimelapse)

        # function to average images at each step             
        def averageimages(self):
                # copies images in output folder to be viewed later if desired
                subprocess.call(["cp /home/pi/BIOE_521_Final_Project/GUI_image_capture/output/*.jpg /home/pi/BIOE_521_Final_Project/GUI_image_capture/saved"],shell=True)
                # calls python function to average images
                os.system('python averageimages.py')
                print ("Saved averaged image")
                # calls python script to remove images in output folder
                os.system('python remove_images.py')

        # zips raw images taken during timelapse for later use (currently not being called in code)
        def ziprawimages(self):
                subprocess.call(["./zipfiles.sh"],shell=True)

        # function to allow user to take a single image (another use case if just want to take images. NOT advised if wishing to focusstack images.)                
	def takeSingleImage(self):
                # grab the current timestamp and use it to construct the
		# output path
                ts = datetime.datetime.now()
                filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
                p = os.path.sep.join((self.outputPath, filename))
                # save the file
                cv2.imwrite(p, self.frame.copy())
                print("[INFO] saved {}".format(filename))


	# function that performs necessary tasks to shut the program
	def onClose(self):
		# set the stop event, cleanup the camera, and allow the rest of
		# the quit process to continue
		print("[INFO] closing...")
		self.stopEvent.set()
		self.vs.stop()
		self.root.quit()
