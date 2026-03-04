import networkx as nx
import matplotlib.pyplot as plt
print("Tharun G Bhat - 4MW23CS175")
G = nx.Graph()
center = 0
nodes = [1, 2, 3, 4, 5]
for n in nodes:
    G.add_edge(center, n)
nx.draw(G, with_labels=True, node_color='red', node_size=800, font_size=10)
plt.title("Star Topology")
plt.show()
