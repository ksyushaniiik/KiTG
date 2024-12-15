import networkx as nx
from collections import deque


def ford_fulkerson(G, source, sink):
    # Создаем копию графа для хранения остаточных пропускных способностей
    R = G.copy()
    
    max_flow = 0
    while True:
        path = bfs(R, source, sink)
        if not path:
            break
        
        flow = float('Inf')
        for u, v in zip(path[:-1], path[1:]):
            flow = min(flow, R[u][v]['capacity'])
            
        for u, v in zip(path[:-1], path[1:]):
            R[u][v]['capacity'] -= flow
            R[v][u]['capacity'] += flow
            
        max_flow += flow
    
    return max_flow


def bfs(R, source, sink):
    visited = {source}
    queue = deque([source])
    parent = {}
    
    while queue:
        u = queue.popleft()
        if u == sink:
            break
        
        for v in R[u]:
            if v not in visited and R[u][v]['capacity'] > 0:
                visited.add(v)
                parent[v] = u
                queue.append(v)
                
    if sink not in parent:
        return None
    
    path = []
    current = sink
    while current != source:
        path.append(current)
        current = parent[current]
    path.append(source)
    path.reverse()
    
    return path

