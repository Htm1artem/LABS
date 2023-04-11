import sys
from pr_Q import PriorityQueue

heap = PriorityQueue()


class Edge:
    def __init__(self, weight, start_peak, target_peak):
        self.weight = weight
        self.start_peak = start_peak
        self.target_peak = target_peak


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacency_list = []
        self.min_distance = sys.maxsize

    def __lt__(self, other):
        self_priority = self.min_distance
        other_priority = other.min_distance
        return self_priority < other_priority


class DijkstraAlgorithm:
    def calculate_shortest_path(self, peak_list, start_peak):
        heap = PriorityQueue()
        start_peak.min_distance = 0
        heap.add(start_peak)

        while not heap.empty():
            actual_peak = heap.get_max()

            for edge in actual_peak.adjacency_list:
                u = edge.start_peak
                v = edge.target_peak
                new_distance = u.min_distance + edge.weight

                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    heap.add(v)

    def get_shortest_path(self, target_peak):
        print(f"Кратчайший путь до вершины: {target_peak.min_distance}")
        node = target_peak
        print("Путь:")

        while node is not None:
            print(f"{node.name}")
            node = node.predecessor