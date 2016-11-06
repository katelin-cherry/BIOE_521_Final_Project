import cv2, platform
import time
import glob,os

#Remove old image files in input folder
image_files="/home/pi/BIOE_521_Final_Project/focusstack/input/*"
r=glob.glob(image_files)
for i in r:
        os.remove(i)


cap= cv2.VideoCapture(0)
if not cap:
        print("!!! Failed VideoCapture: invalid parameter!")
#print ('Default Resolution is ') + str(int(cam.get(3))) + ('x') + str(int(cam.get(4)))
#h=768
#w=1064
#cam.set(3,w)
#cam.set(4,h)
#print ('Now resolution is set to ') + str(w) + ('x') + str(h)


cap.set(3,1280)
cap.set(4,720)


while (True):
    #Capture frame-by-frame
    ret, frame=cap.read()
    if type(frame)==type(None):
        print("!! Couldn't read frame!")
        break

    #Display the resulting fram
    cv2.imshow('Video Test',frame)
    c = cv2.waitKey(1)
    if 's'==chr(c&255):
        endTime=time.time()+60
        while time.time()<endTime:
            img=cap.read()[1]
            cv2.imwrite('/home/pi/BIOE_521_Final_Project/focusstack/input/img{}.png'.format(int(time.time())),frame)
            print 'img'
            time.sleep(.01)
            if cv2.waitKey(1)&0xFF==ord('q'):
                break
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
    #Wait for Excape Key
    #if cv2.waitKey(1)==27:
     #   break
    #key=cv2.waitKey(0)
    #c=cv2.waitKey(0)
    #if 'q'==chr(c&255):
     #   QuitProgram()
    #elif 's'==chr(c&255):
        #while time.time()<endTime:
            #cv2.imwrite('/home/pi/BIOE_521_Final_Project/focusstack/input/img.png'.format(int(time.time())),frame)
            #print 'img'
            #time.sleep(10)
            
cap.release()
cv2.destroyAllWindows()
#cv2.VideoCapture(0).release()
#When everything done, release the capture

