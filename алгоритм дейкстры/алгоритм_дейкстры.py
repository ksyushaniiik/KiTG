
import heapq

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)} # Используем словарь для списка смежности

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))  # Для неориентированного графа
    def dijkstra(self, start_node):
        distances = {node: float('inf') for node in self.adj_list}
        distances[start_node] = 0
        priority_queue = [(0, start_node)]  # (расстояние, вершина)
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                continue # Пропускаем устаревшие расстояния
            for neighbor, weight in self.adj_list[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances
# Пример использования:
num_vertices = 6
graph = Graph(num_vertices)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 1)
graph.add_edge(1, 3, 1)
graph.add_edge(2, 1, 2)
graph.add_edge(2, 3, 5)
graph.add_edge(2, 4, 1)
graph.add_edge(3, 4, 3)
graph.add_edge(3, 5, 2)
graph.add_edge(4, 5, 4)
start_node = 0
shortest_paths = graph.dijkstra(start_node)
print(f"Кратчайшие пути от узла {start_node}: {shortest_paths}")
