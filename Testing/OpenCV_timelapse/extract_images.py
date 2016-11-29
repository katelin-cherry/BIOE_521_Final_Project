import cv2

vidcap = cv2.VideoCapture('big_buck_bunny.mp4')
vidcap.set(cv2.CAP_PROP_POS_MSEC,20000)      # just cue to 20 sec. position
success,image = vidcap.read()
if success:
    cv2.imwrite("frame20sec.jpg", image)     # save frame as JPEG file
    cv2.imshow("20sec",image)
    cv2.waitKey()   
