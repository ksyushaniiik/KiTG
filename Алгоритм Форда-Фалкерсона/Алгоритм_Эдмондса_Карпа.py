import networkx as nx
from collections import deque


def edmonds_karp(G, source, target):
    # �������� ���� ��� �������� ����������� �����
    R = G.copy()
    
    # �������������� ������������ ����� ����
    max_flow = 0
    
    # ���������� ������ ������������� ����, ���� ��� ����������
    while True:
        # ���������� BFS ��� ������ �������������� ����
        path = bfs(R, source, target)
        
        # ���� ���� �� ������, ���������� ������
        if not path:
            break
        
        # ������� ����������� �������� ���������� ����������� �� ��������� ����
        flow = float('inf')
        for u, v in zip(path[:-1], path[1:]):
            flow = min(flow, R[u][v]['capacity'])
        
        # ��������� ������ � ���������� ���������� �����������
        for u, v in zip(path[:-1], path[1:]):
            R[u][v]['capacity'] -= flow
            R[v][u]['capacity'] += flow
        
        # ��������� ��������� ����� � ������ ��������
        max_flow += flow
    
    return max_flow


# ������� ��� ������ �������������� ���� � ������� BFS
def bfs(R, source, target):
    # ��������� ���������� �����
    visited = set()
    # ������� ��� BFS
    queue = deque([source])
    # ������� ������� ��� �������������� ����
    pred = {}
    
    # ��������� BFS
    while queue:
        u = queue.popleft()
        if u == target:
            break
        
        for v in R[u]:
            if v not in visited and R[u][v]['capacity'] > 0:
                visited.add(v)
                pred[v] = u
                queue.append(v)
    
    # ��������������� ����, ���� �� ����������
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


# ������ �������������
if __name__ == "__main__":
    # �������� ������������ ����
    G = nx.DiGraph()
    
    # ������� ���� � �� ����������� �������������
    edges = [
        ('s', 'a', {'capacity': 8}),
        ('s', 'b', {'capacity': 7}),
        ('a', 'c', {'capacity': 9}),
        ('b', 'c', {'capacity': 11}),
        ('c', 't', {'capacity': 12})
    ]
    
    G.add_edges_from(edges)
    
    # ������ ������������ ����� �� ��������� 's' � ����� 't'
    source = 's'
    target = 't'
    max_flow = edmonds_karp(G, source, target)
    
    print(f"������������ �����: {max_flow}")

