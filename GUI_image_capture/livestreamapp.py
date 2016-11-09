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

		# create a button, that when pressed, will take the current
		# frame and save it to file

		btn = tki.Button(self.root, text="Start Image Capture",
			command=self.takeSnapshot)
		btn.pack(side="bottom", fill="both", expand="no", padx=5,
			pady=5)
		
		#create a second button, that when pressed, will focusstack the 
		#images and output the merged image to a window
		btn2 = tki.Button(self.root, text="Focusstack images", command=self.focusstack)
		btn2.pack(side="bottom", fill="both", expand="no", padx = 5, pady=5)
                          

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
				# have a maximum width of 600 pixels
				self.frame = self.vs.read()
				self.frame = imutils.resize(self.frame, width=600)
		
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

       # def timelapse(self):
        #        self.root.after(1000, takeSnapshot)
        
	#function that will perform the focusstacking when btn2 is clicked
        def focusstack(self):
                os.system('python main.py')
                os.system('python load_image.py --image merged.png')
                          
	#function that will take a picture when btn is clicked
	def takeSnapshot(self):
		# grab the current timestamp and use it to construct the
		# output path   
                ts = datetime.datetime.now()
                filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
                p = os.path.sep.join((self.outputPath, filename))

                # save the file
                cv2.imwrite(p, self.frame.copy())
                #cv2.imwrite(filename,image)
                print("[INFO] saved {}".format(filename))

	#function that performs necessary tasks to shut the program
	def onClose(self):
		# set the stop event, cleanup the camera, and allow the rest of
		# the quit process to continue
		print("[INFO] closing...")
		self.stopEvent.set()
		self.vs.stop()
		self.root.quit()
