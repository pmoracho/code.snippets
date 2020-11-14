import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc

mos = np.random.rand(120)
y = np.arange(1,121)

fig, ax = plt.subplots()
plt.scatter(y, mos)

print("hola")

cant = 5
for i in range(0,len(mos),cant):
	lines = []
	for j in range(0,cant-1):
		p = [(y[i+j], mos[i+j]), (y[i+j+1], mos[i+j+1])]
		lines.append(p)

	lc = mc.LineCollection(lines, colors='red', linewidths=1)
	ax.add_collection(lc)

  
plt.title('Imagen 1')
plt.ylabel('MOS')
plt.xlabel('Numero de Imagen')
plt.grid(True)
plt.tight_layout()

plt.show()
