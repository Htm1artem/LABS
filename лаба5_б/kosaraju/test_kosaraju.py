from kosaraju import Graph

g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'A')
g.add_edge('D', 'C')
g.add_edge('D', 'E')
g.add_edge('E', 'F')
g.add_edge('F', 'D')

components = g.kosaraju()

print("Компоненты сильной связности:")
for component in components:
    print(component)