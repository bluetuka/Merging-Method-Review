from collections import deque
from typing import Dict

class FordFulkerson:
    def max_flow(self, graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
        """Ford-Fulkerson algorithm implementation"""
        residual_graph = {u: {v: cap for v, cap in neighbors.items()} 
                         for u, neighbors in graph.items()}
        parent = {}
        max_flow = 0
        
        while self.bfs(residual_graph, source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, residual_graph[parent[s]][s])
                s = parent[s]
                
            max_flow += path_flow
            
            v = sink
            while v != source:
                u = parent[v]
                residual_graph[u][v] -= path_flow
                residual_graph[v][u] += path_flow
                v = u
                
        return max_flow
    
    def bfs(self, graph, source, sink, parent):
        visited = {node: False for node in graph}
        queue = deque()
        queue.append(source)
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            
            for v, capacity in graph[u].items():
                if not visited[v] and capacity > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        return True
        return False
