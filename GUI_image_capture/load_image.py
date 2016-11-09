#import the necessary packages
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args=vars(ap.parse_args())

#reads the merged image
image=cv2.imread(args["image"])

#shows the merged image in a window
cv2.imshow("image", image)
cv2.waitKey(0)
