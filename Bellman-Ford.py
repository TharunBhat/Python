import networkx as nx
print("Tharun G Bhat - 4MW23CS175")
G = nx.DiGraph()
edges = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'C', 3), ('B', 'D', 2),
    ('B', 'E', 3), ('C', 'B', 1),
    ('C', 'D', 4), ('D', 'E', 2)
]
G.add_weighted_edges_from(edges)
source = 'A'
lengths, paths = nx.single_source_bellman_ford(G, source)
print(f"Shortest path tree from {source} using Bellman-Ford:\n")
for node in paths:
    print(f"{source} -> {node}: Path = {paths[node]}, Distance = {lengths[node]}")
