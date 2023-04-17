from tarjan import tarjan_topological_sort
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

sorted_nodes = tarjan_topological_sort(graph)
print(sorted_nodes)

graph = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['D'],
'D': ['E'],
'E': []
}

sorted_nodes = tarjan_topological_sort(graph)
print(sorted_nodes)

graph = {
'A': ['B', 'C'],
'B': ['D'],
'C': ['E'],
'D': ['F'],
'E': ['F'],
'F': []
}

sorted_nodes = tarjan_topological_sort(graph)
print(sorted_nodes) 