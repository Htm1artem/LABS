from kruskal import kruskal

n = 6
edges = [(0, 1, 6), (0, 2, 1), (0, 3, 5), (1, 2, 5), (1, 4, 3), (2, 4, 6), (2, 3, 5), (2, 5, 4), (3, 5, 2), (4, 5, 6)]

mst = kruskal(n, edges)

print("Ребра в минимальном остовном дереве:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} с весом {edge[2]}")