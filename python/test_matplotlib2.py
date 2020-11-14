import matplotlib.pyplot as plt
import numpy as np
t1 = np.arange(0.0, 1.0, 0.02)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
lista_normalizada = [ (n-min(lista))/(max(lista)-min(lista)) for n in lista]
print(lista_normalizada)
for i,n in enumerate(lista):
	print(i)
	plt.plot(t1, t1*n, color=[0.1, lista_normalizada[21-i], lista_normalizada[i]])

plt.show() 
