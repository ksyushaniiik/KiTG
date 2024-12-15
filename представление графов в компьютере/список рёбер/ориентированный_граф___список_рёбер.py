class Graph:
    def __init__(self):
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def get_neighbors(self, u):
        neighbors = []
        for edge in self.edges:
            if edge[0] == u:
                neighbors.append((edge[1], edge[2]))  # (neighbor, weight)
        return neighbors

    def has_edge(self, u, v):
        return any( (u, v, w) for u, v, w in self.edges)

    def __str__(self):
        return str(self.edges)

# Пример использования:
graph = Graph()
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 2)
graph.add_edge(1, 2, 3)
print(graph)  # [(0, 1, 5), (0, 2, 2), (1, 2, 3)]
print(graph.get_neighbors(0))  # [(1, 5), (2, 2)]
print(graph.has_edge(0, 1))  # True


