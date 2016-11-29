# Final Project - Low-cost focusstacking system
**Team 11-House of Pies**
**Melody Tan and Katelin Cherry**

**ABSTRACT**
Microscopy is limited by a trade off between resolution and magnification against depth of field. This results in images that have certain portions that are in-focus and other portions that are out-of-focus, depending on the distance at which they were taken. Focus stacking is an image processing technique where a series of images is captured at different focal distances. The in-focus portions of each image are then combined to form a single, completely in-focus image.
We created a low-cost focus stacking system using a USB microscope to image samples mounted on a Cognisys Stackshot photo stacking platform. The Stackshot is set up to move the sample towards the microscope objective by a constant step size over a specified distance. The USB microscope takes a series of images, which are then processed on the Raspberry Pi using an open-source focus stacking program that we have adapted for our application. Composite images are then automatically saved and displayed on the Raspberry Pi.

**Using the Program**
1. Download the Github zip file or download the source repository.  
2. Navigate to ~/BIOE_521_Final_Project/ in the terminal  
3. Type `python live_stream.py --output output` in the terminal   
4. Plug the USB microscope into the Raspberry Pi and set it up in front of the Stackshot.   
5. The focusstacking window will appear on the screen. There will be a live feed of the USB microscope. Adjust the focus and lighting on the microscope until the front portion of the specimen is in focus.  
6. Enter the desired number of steps and time delay on the Raspberry Pi interface.  
5. Set up the Stackshot on a flat surface and place the specimen on the platform. Turn on the Stackshot and enter the desired number of steps and total distance on the interface.  
6. Click ‘Start’ on the Stackshot interface and immediately click ‘Start Timelapse’ on the Raspberry Pi interface.  
7. Wait until the full series of images has been captured. Click ‘Focus Stack Images’ on the Raspberry Pi interface.  
8. The merged focusstacked image will appear in a new window. Enjoy your pretty picture! It is also saved in the BIOE_521_Final_Project folder.  


 

