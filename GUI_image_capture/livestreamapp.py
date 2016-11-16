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
		#self.count=0

		# initialize the root window and image panel
		self.root = tki.Tk()
		self.panel = None


		#create a second button, that when pressed, will focus stack the 
		#images and output the merged image to a window
		btn2 = tki.Button(self.root, text="Focus Stack images", command=self.focusstack)
		btn2.pack(side="right", expand="no", padx = 5, pady=5)
                          
                #create a third button, that when pressed, will do single image capture
		btn3 = tki.Button(self.root, text="Take Single Image",
			command=self.takeSingleImage)
		btn3.pack(side="right", expand="no", padx=5,
			pady=5)

		# create a button, that when pressed, will take the current
		# frame and save it to file
        
		btn = tki.Button(self.root, text="Start Timelapse",
			command=self.takeSnapshot)
		btn.pack(side="right", expand="no", padx=5,
			pady=5)

                steps_label=tki.Label(self.root, text="Number of Steps")
                steps_entry= tki.Entry(self.root)
                steps_label.pack()
                steps_entry.pack()

                steps_entry.bind("<Return>", self.retrieveinput)

                #btn4 = tki.Button(self.root, text = "Enter", command=self.retrieve_input)
                #btn4.pack(side="right", expand="no", padx=5, pady=5)
                #global countermax
                #countermax=self.steps_entry.get()
                
    
                #countermax= steps.get()

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
        def retrieveinput(self):
                print (self.steps_entry.get())

       # def timelapse(self):
        #        self.root.after(1000, takeSnapshot) 
	#function that will perform the focusstacking when btn2 is clicked
        def focusstack(self):
                global counter


                #ent_count=tki.Entry(Window)
                #ent_count=tki.pack()
                #counter=ent_count.get()
 
                counter=0
                os.system('python remove_low_res.py')
                os.system('python main.py')
                os.system('python load_image.py --image merged.png')

                          
	#function that will take a picture when btn is clicked

        global counter
        counter=0

 
	def takeSnapshot(self):
                #countermax=self.steps_entry.get()
                global counter
                #global countermax
                #global countermax
                #countermax =self.steps.get()
		# grab the current timestamp and use it to construct the
		# output path   
                if (counter<300):
                        ts = datetime.datetime.now()
                        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
                        p = os.path.sep.join((self.outputPath, filename))
                        counter +=1
                        # save the file
                        cv2.imwrite(p, self.frame.copy())
                        print("[INFO] saved {}".format(filename))
                        self.root.after(10000, self.takeSnapshot)
                          
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
