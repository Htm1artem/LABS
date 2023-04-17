def tarjan_topological_sort(graph):
    index_counter = [0]
    stack = []
    lowlinks = {}
    index = {}
    result = []

    def visit(node):
        lowlinks[node] = index[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
        try:
            neighbors = graph[node]
        except:
            neighbors = []
        for neighbor in neighbors:
            if neighbor not in lowlinks:
                visit(neighbor)
                lowlinks[node] = min(lowlinks[node], lowlinks[neighbor])
            elif neighbor in stack:
                lowlinks[node] = min(lowlinks[node], index[neighbor])
        if lowlinks[node] == index[node]:
            component = []
            while True:
                successor = stack.pop()
                component.append(successor)
                if successor == node:
                    break
            result.append(component)
    for node in graph:
        if node not in lowlinks:
            visit(node)
    result.reverse()
    sorted_nodes = []
    for component in result:
        sorted_nodes.extend(component)
    return sorted_nodes