class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            if self.size[pi] < self.size[pj]:
                pi, pj = pj, pi
            self.parent[pj] = pi
            self.size[pi] += self.size[pj]


def kruskal(n, edges):
    uf = UnionFind(n)
    mst = []
    edges.sort(key=lambda e: e[2])
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
    return mst