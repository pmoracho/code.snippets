import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations

nodes = {
"1": [100,0,0,0,0,0,0,0],
"2": [0,25,0,25,25,25,0,0], 
"3": [0,0,50,0,30,0,20,0], 
"4": [0,0,0,100,0,0,0,0],
"5": [0,0,0,0,10,10,0,80], 
"6": [0,0,0,0,0,100,0,0], 
"7": [0,0,0,0,0,70,30,0], 
"8": [0,0,0,0,0,0,0,100]}

pairs = [("1", "2"), ("3", "4"), ("5", "6"), ("7", "8")]
edges = combinations(nodes, 2)
g = nx.Graph()
plt.subplot(121)

g.add_nodes_from(nodes)
g.add_edges_from(pairs) 

nx.draw(g, with_labels=True, font_weight='bold')
plt.show()



