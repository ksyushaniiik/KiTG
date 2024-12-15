class Graph:
    def __init__(self):
        self.edges = set()  # »спользуем множество дл€ предотвращени€ дубликатов

    def add_edge(self, u, v):
        self.edges.add(tuple(sorted((u, v)))) # tuple дл€ хешировани€, sorted дл€ неориентированного графа

    def get_neighbors(self, u):
        neighbors = set()
        for edge in self.edges:
            if u in edge:
                neighbors.add(edge[1-edge.index(u)])
        return list(neighbors) #преобразуем в список

    def has_edge(self, u, v):
        return tuple(sorted((u, v))) in self.edges

    def __str__(self):
        return str(list(self.edges)) #преобразуем в список дл€ вывода


# ѕример использовани€:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
print(graph)  # [(0, 1), (0, 2), (1, 2)]
print(graph.get_neighbors(0))  # [1, 2]
print(graph.has_edge(0, 1))  # True

