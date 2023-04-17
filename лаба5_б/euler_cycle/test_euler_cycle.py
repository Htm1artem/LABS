from euler_cycle import Graph


g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(4, 7)
g.add_edge(7, 5)
g.add_edge(5, 8)
g.add_edge(8, 6)

cycle = g.find_eulerian_cycle()

if cycle:
    print("Eulerian cycle: ", cycle)
else:
    print("No Eulerian cycle found")
