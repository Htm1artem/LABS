from Dijkstra import Node, Edge, DijkstraAlgorithm
from pr_Q import PriorityQueue 
# Создаем вершины графа
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

# Создаем ребра графа
A.adjacency_list.append(Edge(10, A, B))
A.adjacency_list.append(Edge(15, A, C))
B.adjacency_list.append(Edge(12, B, D))
B.adjacency_list.append(Edge(15, B, F))
C.adjacency_list.append(Edge(10, C, E))
D.adjacency_list.append(Edge(1, D, E))
D.adjacency_list.append(Edge(2, D, F))
F.adjacency_list.append(Edge(5, F, E))

# Создаем алгоритм Дейкстры и вызываем его для вершины A
algorithm = DijkstraAlgorithm()
algorithm.calculate_shortest_path([A, B, C, D, E, F], A)

# Проверяем, что кратчайшие пути расчитаны верно
assert B.min_distance == 10
print("Кратчайший путь до B расчитан верно")
assert C.min_distance == 15
print("Кратчайший путь до C расчитан верно")
assert D.min_distance == 22
print("Кратчайший путь до D расчитан верно")
assert E.min_distance == 23
print("Кратчайший путь до E расчитан верно")
assert F.min_distance == 25
print("Кратчайший путь до F расчитан верно")

# Проверяем, что пути до вершин расчитаны верно
assert algorithm.get_shortest_path(E) == "A -> C -> E"
print("Путь до E расчитан верно")
assert algorithm.get_shortest_path(F) == "A -> B -> F"
print("Путь до F расчитан верно")