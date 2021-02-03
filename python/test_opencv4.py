import cv2
import numpy as np
import imutils

img = cv2.imread('../../../Descargas/xIDar.jpg', 1)

############################################################################
# Remover colores
############################################################################
lower = np.array([200, 200, 200])
upper = np.array([255, 255, 255])
shape = cv2.inRange(img, lower, upper)
shape = cv2.bitwise_not(shape)

cv2.imshow("Solo ciertos colores", shape)
cv2.waitKey(0)


############################################################################
# Armo la máscara de selección
############################################################################
nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(shape, connectivity=8)
sizes = stats[1:, -1]
nb_components = nb_components - 1
clean_mask = np.zeros((output.shape[0], output.shape[1], 3), dtype="uint8")

for i in range(0, nb_components):
    # print(sizes[i])
    if sizes[i] >= 10000:
        clean_mask[output == i + 1] = 255


cv2.imshow("Clean MASK", clean_mask)
cv2.waitKey(0)

def dilatation(val):
    dilatation_size = cv2.getTrackbarPos(title_trackbar_kernel_size, title_dilation_window)
    dilation_shape = morph_shape(cv2.getTrackbarPos(title_trackbar_element_shape, title_dilation_window))
    element = cv2.getStructuringElement(dilation_shape, (2 * dilatation_size + 1, 2 * dilatation_size + 1),
                                       (dilatation_size, dilatation_size))
    dilatation_dst = cv2.dilate(src, element)
    cv.imshow(title_dilation_window, dilatation_dst)