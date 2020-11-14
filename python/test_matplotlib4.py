import matplotlib.pyplot as plt
from random import randint

w,h = (3,9)

# Ejemplo con solución de una sola diagonal
sensores = [
	[[0, w], [2, h]],
	[[0, w], [4, 4]],
	[[0, w], [8, 7]],
]	

# Ejemplo con solución usando las dos diagonales
sensores = [
	[[0, w], [2, h]],
	[[0, w], [4, 4]],
	[[0, w], [8, 7]],
	[[1, w], [h, 3]],
	[[2, w], [0, 2]],
]	

diagonales = [
	[[0, w], [0, h]],
	[[0, w], [h, 0]]
]

cantidad_sensores = len(sensores)

# Dibujamos el camino de los sensores
for x,y in sensores:
	plt.plot(x,y, marker = 'o', color='blue')

# Verificamos cada diagonal, si una sola corta el total de sensores
# esta será nuestra respuesta sino serán las dos diagonales
diag_ok = None
for xd,yd in diagonales:
	corta = 0
	for xs,ys in sensores:
		print("diag: {0}:{1}  sensor {2}:{3}".format(xd, yd, xs, ys))
		
		if (xs[0] <= xd[0] and ys[1] > yd[1]) or (xs[0] >= xd[0] and ys[1]< yd[1]):
			corta = corta + 1

	if corta == cantidad_sensores:
		diag_ok = [xd,yd]
		break

if diag_ok is not None:
	plt.plot(diag_ok[0], diag_ok[1], marker = 'o', color='red', linestyle = 'dashdot')
else:		
	for x,y in diagonales:
		plt.plot(x,y, marker = 'o', color='red', linestyle = 'dashdot')

plt.axis([0,w,0,h])
plt.show()

