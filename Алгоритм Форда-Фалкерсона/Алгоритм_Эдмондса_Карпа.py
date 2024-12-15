import networkx as nx
from collections import deque


def edmonds_karp(G, source, target):
    # Копируем граф для хранения остаточного графа
    R = G.copy()
    
    # Инициализируем максимальный поток нулём
    max_flow = 0
    
    # Продолжаем искать увеличивающие пути, пока они существуют
    while True:
        # Используем BFS для поиска увеличивающего пути
        path = bfs(R, source, target)
        
        # Если путь не найден, прекращаем работу
        if not path:
            break
        
        # Находим минимальное значение пропускной способности на найденном пути
        flow = float('inf')
        for u, v in zip(path[:-1], path[1:]):
            flow = min(flow, R[u][v]['capacity'])
        
        # Обновляем потоки и остаточные пропускные способности
        for u, v in zip(path[:-1], path[1:]):
            R[u][v]['capacity'] -= flow
            R[v][u]['capacity'] += flow
        
        # Добавляем найденный поток к общему значению
        max_flow += flow
    
    return max_flow


# Функция для поиска увеличивающего пути с помощью BFS
def bfs(R, source, target):
    # Множество посещённых узлов
    visited = set()
    # Очередь для BFS
    queue = deque([source])
    # Словарь предков для восстановления пути
    pred = {}
    
    # Выполняем BFS
    while queue:
        u = queue.popleft()
        if u == target:
            break
        
        for v in R[u]:
            if v not in visited and R[u][v]['capacity'] > 0:
                visited.add(v)
                pred[v] = u
                queue.append(v)
    
    # Восстанавливаем путь, если он существует
    if target not in pred:
        return None
    
    path = []
    current = target
    while current != source:
        path.append(current)
        current = pred[current]
    path.append(source)
    path.reverse()
    
    return path


# Пример использования
if __name__ == "__main__":
    # Создадим направленный граф
    G = nx.DiGraph()
    
    # Добавим рёбра с их пропускными способностями
    edges = [
        ('s', 'a', {'capacity': 8}),
        ('s', 'b', {'capacity': 7}),
        ('a', 'c', {'capacity': 9}),
        ('b', 'c', {'capacity': 11}),
        ('c', 't', {'capacity': 12})
    ]
    
    G.add_edges_from(edges)
    
    # Найдем максимальный поток от источника 's' к стоку 't'
    source = 's'
    target = 't'
    max_flow = edmonds_karp(G, source, target)
    
    print(f"Максимальный поток: {max_flow}")

