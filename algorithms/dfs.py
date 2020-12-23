def dfs(graph, node, visited=[]):
    if node not in visited:
        visited.append(node)
        print(node)
        for neighbor in graph.get_neighbors(node):
            if neighbor not in visited:
                dfs(graph, neighbor, visited)