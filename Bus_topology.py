import networkx as nx
import matplotlib.pyplot as plt
print("Tharun G Bhat - 4MW23CS175")
G = nx.path_graph(6)
nx.draw(G, with_labels=True, node_color='cyan', node_size=800)
plt.title("Bus Topology")
plt.show()
