from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.vertices.add(u)
        self.vertices.add(v)

    def find_eulerian_cycle(self):
        if not self.is_eulerian():
            return None

        graph = defaultdict(list)
        for u in self.vertices:
            graph[u] = self.graph[u][:]

        cycle = []
        stack = [next(iter(self.vertices))]

        while stack:
            u = stack[-1]

            if graph[u]:
                v = graph[u].pop()
                graph[v].remove(u)
                stack.append(v)
            else:
                cycle.append(stack.pop())

        return cycle[::-1]

    def is_eulerian(self):
        for u in self.vertices:
            if len(self.graph[u]) % 2 != 0:
                return False

        visited = set()
        self.dfs(next(iter(self.vertices)), visited)

        return len(visited) == len(self.vertices)

    def dfs(self, u, visited):
        visited.add(u)
        for v in self.graph[u]:
            if v not in visited:
                self.dfs(v, visited)