
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

class LiveStreamApp:
	def __init__(self, vs, outputPath):
		# store the video stream object and output path, then initialize
		# the most recently read frame, thread for reading frames, and
		# the thread stop event
		self.vs = vs
		self.outputPath = outputPath
		self.frame = None
		self.thread = None
		self.stopEvent = None

		# initialize the root window and image panel
		self.root = tki.Tk()
		self.panel = None

                #user input for number of steps
		steps_label = tki.Label(self.root, text="Number of Steps")
		#steps_label.grid(row=1, column=1, padx=5, pady=5)
 		steps_label.pack(side="bottom") #, expand="no", padx=5, pady=5)
                self.steps_entry = tki.Entry(self.root)
                #self.steps_entry.grid(row=2, column=1)
                self.steps_entry.pack(side="bottom") #, expand="no", padx=5, pady=5)

 		#user input for time per step (s)
 		time_label = tki.Label(self.root, text="Time per Step")
                #time_label.grid(row=4, column=1, padx=5, pady=5)
 	        time_label.pack(side="bottom") #, expand="no", padx=5, pady=5)
 		self.time_entry = tki.Entry(self.root)
 		#self.time_entry.grid(row=5, column=1)
 		self.time_entry.pack(side="bottom")

 	        #Take Single Image button
		btn3 = tki.Button(self.root, text="Take Single Image",
		command=self.takeSingleImage)
		#btn3.grid(row=7, column=1, padx=5, pady=5)
		btn3.pack(side="right", expand="no", padx=5, pady=5)

                #Start Timelapse button
 	        btn = tki.Button(self.root, text="Start Timelapse",
		command=self.takeSnapshot)
 	        #btn.grid(row=9, column=1, padx=5, pady=5)
		btn.pack(side="bottom", expand="no", padx=5, pady=5)

		#creates a buttton that when pressed, will focus stack the 
		#images and output the merged image to a window
		btn2 = tki.Button(self.root, text="Focus Stack images", command=self.focusstack)
		#btn2.grid(row=10, column=1, padx=5, pady=5)
		btn2.pack(side="right", expand="no", padx=5, pady=5)

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


	#function that will perform the focusstacking when btn2 is clicked
        def focusstack(self):
                global counter
                counter=0
                os.system('python remove_low_res.py')
                os.system('python main.py')
                os.system('python load_image.py --image merged.png')

                          
	#function that will take a picture when btn is clicked
        global counter
        counter=0
 
	def takeSnapshot(self):
                global counter
		# grab the current timestamp and use it to construct the
		# output path
		numSteps = int(self.steps_entry.get())
		timePerStep = int(self.time_entry.get())
		msPerStep = int(timePerStep*1000)
                if (counter<numSteps):
                        ts = datetime.datetime.now()
                        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
                        p = os.path.sep.join((self.outputPath, filename))
                        counter +=1
                        # save the file
                        cv2.imwrite(p, self.frame.copy())
                        print("[INFO] saved {}".format(filename))
                        self.root.after(msPerStep, self.takeSnapshot)
                
                          
	def takeSingleImage(self):
                ts = datetime.datetime.now()
                filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
                p = os.path.sep.join((self.outputPath, filename))
                # save the file
                cv2.imwrite(p, self.frame.copy())
                print("[INFO] saved {}".format(filename))


	#function that performs necessary tasks to shut the program
	def onClose(self):
		# set the stop event, cleanup the camera, and allow the rest of
		# the quit process to continue
		print("[INFO] closing...")
		self.stopEvent.set()
		self.vs.stop()
		self.root.quit()
