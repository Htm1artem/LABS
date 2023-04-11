from bfs import BFS

def test_bfs():
    graph = {'A': ['B', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F'],
             'D': ['B'],
             'E': ['B', 'F'],
             'F': ['C', 'E']}

    bfs = BFS(graph)
    bfs.bfs('A')
    assert bfs.visited_nodes == set(['A', 'B', 'C', 'D', 'E', 'F'])

test_bfs()