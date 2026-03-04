import networkx as nx
import matplotlib.pyplot as plt
print("Tharun G Bhat - 4MW23CS175")
G = nx.complete_graph(5)
nx.draw(G, with_labels=True, node_color='yellow', node_size=800)
plt.title("Mesh Topology")
plt.show()
