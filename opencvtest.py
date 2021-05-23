# python opencvtest.py -i OpenCV_Logo.png
import cv2
import argparse
import imutils
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="OpenCV_Logo.png", help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("OpenCV", image)
# cv2.waitKey(0)

img2 = imutils.rotate(image, 40)
# cv2.imshow("Rotated", img2)

img3 = imutils.rotate_bound(image, 60)
# cv2.imshow("Rotate bounded", img3)

# Color spaces

nimg = np.ones(image.shape, dtype=np.uint8) * 100
# cv2.imshow("nimg", nimg)

updated_img = cv2.add(image, nimg)
# cv2.imshow("Updated", updated_img)

subt = cv2.subtract(image, nimg)
# cv2.imshow("subtracted", subt)

img4 = image[:, :, 2]
# cv2.imshow("channeltest", img4)
# print(image.shape)
# print(img4.shape)
red = (0, 0, 255)
canvas = np.ones((500, 500, 3), dtype=np.uint8)
cv2.imshow("before rect", canvas)
canvas = cv2.rectangle(canvas, (100, 100), (350, 350), red, -1)
# canvas = cv2.rectangle(image, (50, 50), (80, 80), red, -1)
cv2.imshow("canvas", canvas)

cv2.waitKey(0)
print("End")