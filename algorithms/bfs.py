import graph

def bfs(graph, root, queue=[], visited=[]):
    queue.append(root)
    visited.append(root)

    while queue:
        node = queue.pop(0)
        print(node)
        for neighbor in graph.get_neighbors(node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    print()

