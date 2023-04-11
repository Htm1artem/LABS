class FloydWarshall():

    def __init__(self, graph=[]):
        if not graph:
            raise Exception('Empty graph provided.')
        self.graph = graph
        self.vertices_count = 0
        self.paths = []

    def calculate_shortest_paths(self):
        self.vertices_count = len(self.graph)
        distances = self.graph.copy()
        self.paths = [[None for x in range(self.vertices_count)] for y in range(self.vertices_count)]
        for v in range(self.vertices_count):
            for u in range(self.vertices_count):
                if v == u:
                    self.paths[v][u] = 0
                elif distances[v][u] != float('inf'):
                    self.paths[v][u] = v
                else:
                    self.paths[v][u] = -1
        for k in range(self.vertices_count):
            for v in range(self.vertices_count):
                for u in range(self.vertices_count):
                    if distances[v][k] != float('inf') and distances[k][u] != float('inf') \
                            and (distances[v][k] + distances[k][u] < distances[v][u]):
                        distances[v][u] = distances[v][k] + distances[k][u]
                        self.paths[v][u] = self.paths[k][u]
                if distances[v][v] < 0:
                    print('Обнаружен отрицательный цикл.')
                    return

    def print_shortest_paths(self):
        def print_path(paths, v, u, route):
            if paths[v][u] == v:
                return
            print_path(paths, v, paths[v][u], route)
            route.append(paths[v][u])
        for v in range(self.vertices_count):
            for u in range(self.vertices_count):
                if u != v and self.paths[v][u] != -1:
                    route = [v]
                    print_path(self.paths, v, u, route)
                    route.append(u)
                    print(f'Кратчайший путь из вершины {v} к вершине {u}:', route)