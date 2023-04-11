from dfs import DFS


def test_dfs():
    graph = {'A': ['B', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F'],
             'D': ['B'],
             'E': ['B', 'F'],
             'F': ['C', 'E']}

    dfs = DFS(graph)
    dfs.dfs('A')
    assert dfs.visited == set(['A', 'B', 'D', 'E', 'F', 'C'])


test_dfs()