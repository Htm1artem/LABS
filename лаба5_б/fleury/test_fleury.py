from collections import defaultdict
from fleury import Graph, fleury_algorithm

g = Graph(6)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)

path = fleury_algorithm(g)

if path:
    print("Эйлеров путь:", "->".join(str(v) for v in path))
else:
    print("Путь Эйлера не найден.")

g = Graph(5)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.add_edge(2, 4)
g.add_edge(4, 0)

path = fleury_algorithm(g)

if path:
    print("Эйлеров путь:", "->".join(str(v) for v in path))
else:
    print("Путь Эйлера не найден.")