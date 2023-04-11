from f_w import FloydWarshall

adj_matrix = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

fw = FloydWarshall(adj_matrix)
fw.calculate_shortest_paths()

fw.print_shortest_paths()