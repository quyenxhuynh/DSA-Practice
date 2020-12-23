class Graph:
    def __init__(self):
        self.graph = {}
    
    def add(self, origin, destination):
        if origin in self.graph:
            self.graph[origin].append(destination)
        else:
            self.graph[origin] = [destination]
        
        if destination not in self.graph:
            self.graph[destination] = []
    
    def remove(self, origin, destination):
        if destination in self.graph[origin]:
            self.graph[origin].remove(destination)
        
    def get_neighbors(self, origin):
        return self.graph[origin]