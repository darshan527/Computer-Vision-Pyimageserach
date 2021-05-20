# python opencvtest.py -i OpenCV_Logo.png
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="OpenCV_Logo.png", help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("OpenCV", image)
# cv2.waitKey(0)

img2 = imutils.rotate(image, 40)
cv2.imshow("Rotated", img2)

img3 = imutils.rotate_bound(image, 60)
cv2.imshow("Rotate bounded", img3)
cv2.waitKey(0)
print("End")