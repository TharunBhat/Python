import networkx as nx
import matplotlib.pyplot as plt
print("Tharun G Bhat - 4MW23CS175")
G = nx.cycle_graph(6)
nx.draw_circular(G, with_labels=True, node_color='blue', node_size=800)
plt.title("Ring Topology")
plt.show()
