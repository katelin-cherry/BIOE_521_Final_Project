import cv2
import time

cap= cv2.VideoCapture(0)
#print ('Default Resolution is ') + str(int(cam.get(3))) + ('x') + str(int(cam.get(4)))
#h=768
#w=1064
#cam.set(3,w)
#cam.set(4,h)
#print ('Now resolution is set to ') + str(w) + ('x') + str(h)

cap.set(3,1280)
cap.set(4,720)
#endTime=time.time()+60

while (True):
    #Capture frame-by-frame
    ret, frame=cap.read()

    #Display the resulting fram
    cv2.imshow('Video Test',frame)

    #Wait for Excape Key
    if cv2.waitKey(1)==27:
        break
    key=cv2.waitKey(0)
    c=cv2.waitKey(0)
    if 'q'==chr(c&255):
        QuitProgram()
    #elif 's'==chr(c&255):
        #while time.time()<endTime:
            #cv2.imwrite('/home/pi/BIOE_521_Final_Project/focusstack/input/img.png'.format(int(time.time())),frame)
            #print 'img'
            #time.sleep(10)
            

cv2.destroyAllWindows()
cv2.VideoCapture(0).release()
#When everything done, release the capture

