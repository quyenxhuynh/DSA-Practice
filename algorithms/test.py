import graph, dfs, bfs

g = graph.Graph()
assert(g.graph == {})

g.add('A', 'B')
g.add('A', 'C')
g.add('B', 'D')
g.add('B', 'E')
g.add('C', 'F')
g.add('E', 'F')

assert(g.graph == {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
})

# dfs.dfs(g, 'A')
# bfs.bfs(g, 'A')