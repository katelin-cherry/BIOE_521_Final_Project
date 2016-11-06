import cv2

vidcap = cv2.VideoCapture('my_video-3.mkv')
#vidcap.set(cv2.CAP_PROP_POS_MSEC,20000)      # just cue to 20 sec. position
success,image = vidcap.read()
count = 0
success=True

while success:
    sucess,image=vidcap.read()
    print ('Read a new frame: '), success
    cv2.imwrite("frame%d.jpg" % count, image)
    count += 1
    
