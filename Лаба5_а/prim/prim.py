class PrimsAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
        self.parent = [None] * self.V
        self.key = [float('inf')] * self.V
        self.mstSet = [False] * self.V
        self.result = {}

    def printMST(self):
        print("Ребра минимального остовного дерева:")
        for key in self.result:
            print(f'{key[0]} - {key[1]}: {self.result[key]}')

    def prim(self):
        self.key[0] = 0
        self.parent[0] = -1
        for i in range(self.V - 1):
            u = self._min_key()
            self.mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] and not self.mstSet[v] and self.graph[u][v] < self.key[v]:
                    self.parent[v] = u
                    self.key[v] = self.graph[u][v]
        self._form_result()

    def _min_key(self):
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if self.key[v] < min_val and not self.mstSet[v]:
                min_val = self.key[v]
                min_index = v
        return min_index

    def _form_result(self):
        for i in range(1, self.V):
            key = (self.parent[i], i)
            self.result[key] = self.graph[i][self.parent[i]]
