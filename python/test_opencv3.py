from skimage.measure import compare_ssim
import imutils
import numpy as np
import cv2

clean = cv2.imread('clean.jpg')
post = cv2.imread('pro.jpg')

cleanG = cv2.cvtColor(clean, cv2.COLOR_BGR2GRAY)
postG = cv2.cvtColor(post, cv2.COLOR_BGR2GRAY)

(score, diff) = compare_ssim(cleanG, postG, full=True)
diff = (diff * 255).astype("uint8")

thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)

for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(clean, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(post, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
# show the output images
# cv2.imshow("Original", clean)
cv2.imshow("Diff", diff)
# cv2.imshow("Thresh", thresh)

cv2.imshow("Modified", post)
cv2.waitKey(0)