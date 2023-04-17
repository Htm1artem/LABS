class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append(end)

    def kosaraju(self):
        visited = set()
        stack = []

        def dfs1(node):
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs1(neighbor)
            stack.append(node)

        for node in self.graph:
            if node not in visited:
                dfs1(node)

        visited = set()
        components = []

        def dfs2(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs2(neighbor, component)

        while stack:
            node = stack.pop()
            if node not in visited:
                component = []
                dfs2(node, component)
                components.append(component)

        return components