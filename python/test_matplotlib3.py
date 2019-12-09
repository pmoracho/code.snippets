import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

params = [
	[100, 0.3,  1, -2],
	[200, 0.5, .8, .3],
	[200, 0.5, .3, .2],
	[200, 0.5, .5, .9],
]

colors = cm.rainbow(np.linspace(0, 1, len(params)))
for i,(cant, sd, x, y) in enumerate(params):
	points =  np.random.randn(cant,2)*sd +[x, y]
	plt.scatter(points[:,0],points[:,1], c=colors[i], alpha=.5)

plt.show()

