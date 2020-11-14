from urllib import request
import cv2
import numpy as np

imgfile = "tB5xQ.png"
request.urlretrieve ("https://i.stack.imgur.com/tB5xQ.png", imgfile)


img_gray = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Gray", img_gray)
cv2.waitKey(0)

thresh = 127
img_bw = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("B/W", img_bw)
cv2.waitKey(0)

"""
(thresh, img_bw) = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("B/W", img_bw)
cv2.waitKey(0)
"""

kernel = np.ones((2,2),np.uint8)
img_bw_erosion = cv2.erode(img_bw, kernel, iterations = 1)


cv2.imshow("Erosions", img_bw_erosion)
cv2.waitKey(0)