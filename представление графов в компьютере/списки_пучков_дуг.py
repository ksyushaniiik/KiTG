class Graph:
    def __init__(self):
        self.edge_bundles = {}  # Словарь: ключ - вершина, значение - список (вершина, вес)

    def add_edge(self, u, v, weight=1):  # weight по умолчанию 1
        if u not in self.edge_bundles:
            self.edge_bundles[u] = []
        self.edge_bundles[u].append((v, weight))

    def get_neighbors(self, u):
        if u in self.edge_bundles:
            return self.edge_bundles[u]
        return []

    def has_edge(self, u, v):
        return any(neighbor == v for neighbor, weight in self.get_neighbors(u))

    def __str__(self):
        return str(self.edge_bundles)


# Пример использования:
graph = Graph()
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 2)
graph.add_edge(1, 2, 3)
graph.add_edge(1,3,1)
print(graph)  # {0: [(1, 5), (2, 2)], 1: [(2, 3),(3,1)]}
print(graph.get_neighbors(0))  # [(1, 5), (2, 2)]
print(graph.has_edge(0, 1))  # True


