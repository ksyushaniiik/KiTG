class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adjacency_matrix[u][v] = 1
            self.adjacency_matrix[v][u] = 1  # Неориентированный граф

    def get_neighbors(self, u):
        if 0 <= u < self.num_vertices:
            neighbors = []
            for v in range(self.num_vertices):
                if self.adjacency_matrix[u][v] == 1:
                    neighbors.append(v)
            return neighbors
        else:
            return []

    def has_edge(self, u, v):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            return self.adjacency_matrix[u][v] == 1
        else:
            return False

    def __str__(self):
        return str(self.adjacency_matrix)

# Пример использования:
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
print(graph)  # [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
print(graph.get_neighbors(0))  # [1, 2]
print(graph.has_edge(0, 1))  # True



