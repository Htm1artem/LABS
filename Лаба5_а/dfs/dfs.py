class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()

    def dfs(self, start):
        self.visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph[start]:
            if neighbor not in self.visited:
                self.dfs(neighbor)