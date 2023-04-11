class BFS:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        self.visited_nodes = set()
        self.queue = []

    def bfs(self, start_node):
        self.visited_nodes.add(start_node)
        self.queue.append(start_node)

        while self.queue:
            current_node = self.queue.pop(0)
            print(current_node, end=" ")

            for neighbour in self.adjacency_list[current_node]:
                if neighbour not in self.visited_nodes:
                    self.visited_nodes.add(neighbour)
                    self.queue.append(neighbour)