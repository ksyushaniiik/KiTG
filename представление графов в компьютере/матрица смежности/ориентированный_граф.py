
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]  # inf для отсутствующих ребер

        for i in range(num_vertices):
          self.adjacency_matrix[i][i] = 0 #петли невозможны

    def add_edge(self, u, v, weight):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adjacency_matrix[u][v] = weight

    def get_neighbors(self, u):
        neighbors = []
        if 0 <= u < self.num_vertices:
            for v in range(self.num_vertices):
                if self.adjacency_matrix[u][v] != float('inf'):
                    neighbors.append((v, self.adjacency_matrix[u][v])) #вершина, вес
        return neighbors


    def has_edge(self, u, v):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            return self.adjacency_matrix[u][v] != float('inf')
        else:
            return False

    def __str__(self):
        return str(self.adjacency_matrix)

# Пример использования:
graph = Graph(4)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 2)
graph.add_edge(1, 2, 3)
print(graph)
print(graph.get_neighbors(0))  # [(1, 5), (2, 2)]
print(graph.has_edge(0, 1))  # True

