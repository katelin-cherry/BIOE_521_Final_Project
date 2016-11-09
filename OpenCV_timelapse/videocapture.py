import cv2

cam=cv2.VideoCapture(0)
output=cv2.VideoWriter('/home/pi/BIOE_521_Final_Project/OpenCV_timelapse/Video.avi',cv2.cv.CV_FOURCC(*'WMV2'),40.0,(640,480))

while (cam.isOpened()):
    ret,frame=cam.read()
    if ret==True:
        output.write(frame)
        cv2.imshow('VideoStream',frame)
        if cv2.waitKey(1)==27:
            break
        else:
            break

cam.release()
output.release()

cv2.destroyAllWindows()
