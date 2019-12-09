import cv2
import urllib.request
import numpy as np
import pprint

req = urllib.request.urlopen('http://www.garuyo.com/sites/default/files/styles/large/public/images/2014/12/tom-waits-en-el-cine_133709.jpg_600512367.jpg')
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1)

windowName = "MiVentana"
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
cv2.resizeWindow(windowName,800,700)
cv2.moveWindow(windowName,0,0)
cv2.setWindowTitle(windowName,"Esta es mi ventana")
cv2.imshow(windowName,img)

# Ahora cambiamos el titulo
if cv2.waitKey():
   cv2.setWindowTitle(windowName, "Nuevo titulo")

# Ahora cambiamos el titulo
if cv2.waitKey():
   cv2.setWindowTitle(windowName, "Otro titulo")

if cv2.waitKey():
   cv2.destroyAllWindows()

"""
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv = img

cv2.imshow('Este es el primer titulo', hsv)
if cv2.waitKey() == ord('q'):
   cv2.setWindowTitle("'Este es el primer titulo'", "Nuevo título")

if cv2.waitKey() == ord('q'):
   cv2.destroyAllWindows()

colors, count = np.unique(hsv.reshape(-1, hsv.shape[-1]), axis=0, return_counts=True)
print(colors[np.argsort(-count)][:5])

for c in colors[np.argsort(-count)][0:100]:
	hsv[np.where((hsv==c).all(axis=2))] = [255,255,255]

cv2.imshow('Test2', hsv)
if cv2.waitKey() == ord('q'):
   cv2.destroyAllWindows()
"""

"""
pprint.pprint(count[count.argmax()])
pprint.pprint(count)

pprint.pprint(np.array((colors, count)).T)
count[::-1].sort()
pprint.pprint(colors[count[0:5])

pprint.pprint(colors[sorted(count, reverse=True), ])
pprint.pprint(count)
pprint.pprint(colors[count.argmax()])
"""

"""
    return colors[count.argmax()]


hist = cv2.calcHist([img],[0],None,[256],[0,256])
colors = sorted([(i, e[0]) for i, e in enumerate(hist) if e[0] > 0], key=lambda x: x[1], reverse=True)

"""


