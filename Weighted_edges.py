import networkx as nx
print("Tharun G Bhat - 4MW23CS175")
G = nx.Graph()
edges = [
    ('A', 'B', 1), ('B', 'C', 2),
    ('C', 'D', 1), ('D', 'E', 3),
    ('A', 'E', 10)
]
G.add_weighted_edges_from(edges)
print("Shortest path A -> E (Before Failure):", nx.shortest_path(G, 'A', 'E', weight='weight'))
G.remove_edge('C', 'D')
print("\nLink between C and D has failed!")
print("Shortest path A -> E (After Failure):", nx.shortest_path(G, 'A', 'E', weight='weight'))
