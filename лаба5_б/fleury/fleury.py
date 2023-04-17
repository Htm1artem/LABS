from collections import defaultdict
 
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.visited = [False] * vertices
 
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    def is_cyclic(self):
        for i in range(self.vertices):
            if not self.visited[i]:
                if self.dfs(i, -1):
                    return True
        return False
 
    def dfs(self, vertex, parent):
        self.visited[vertex] = True
        for i in self.graph[vertex]:
            if not self.visited[i]:
                if self.dfs(i, vertex):
                    return True
            elif parent != i:
                return True
        return False
 
 
def find_bridges(graph):
    bridges = []
    visited = [False] * graph.vertices
    low = [float("inf")] * graph.vertices
    parent = [-1] * graph.vertices
 
    def dfs(vertex):
        visited[vertex] = True
        low[vertex] = ids[vertex] = dfs.t
        dfs.t += 1
        for i in graph.graph[vertex]:
            if not visited[i]:
                parent[i] = vertex
                dfs(i)
                low[vertex] = min(low[vertex], low[i])
                if ids[vertex] < low[i]:
                    bridges.append((vertex, i))
            elif i != parent[vertex]:
                low[vertex] = min(low[vertex], ids[i])
 
    dfs.t = 0
    ids = [0] * graph.vertices
    for i in range(graph.vertices):
        if not visited[i]:
            dfs(i)
 
    return bridges
 

def fleury_algorithm(graph):
    if graph.is_cyclic():
        return None
 
    edges = defaultdict(list)
    for u, v in find_bridges(graph):
        edges[u].append(v)
        edges[v].append(u)
 
    start_vertex = 0
    for i in range(graph.vertices):
        if len(graph.graph[i]) % 2 == 1:
            start_vertex = i
            break
 
    visited = []
 
    def dfs(vertex):
        while edges[vertex]:
            i = edges[vertex].pop()
            if (vertex, i) not in visited and (i, vertex) not in visited:
                visited.append((vertex, i))
                dfs(i)
        path.append(vertex)
 
    path = []
    dfs(start_vertex)
    path.reverse()
 
    return path