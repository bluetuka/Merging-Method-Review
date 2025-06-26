from collections import deque
from typing import Dict

class EdmondsKarp:
    def max_flow(self, graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
        """Edmonds-Karp algorithm implementation (Ford-Fulkerson with BFS)"""
        residual_graph = {u: {v: cap for v, cap in neighbors.items()} 
                         for u, neighbors in graph.items()}
        max_flow = 0
        
        while True:
            # Find an augmenting path using BFS
            path, path_flow = self.find_augmenting_path(residual_graph, source, sink)
            if path_flow == 0:
                break
                
            max_flow += path_flow
            
            # Update residual capacities
            current = sink
            for i in range(len(path) - 1, 0, -1):
                previous = path[i - 1]
                residual_graph[previous][current] -= path_flow
                if residual_graph[previous][current] == 0:
                    del residual_graph[previous][current]
                    
                # Update reverse edge
                if current not in residual_graph.get(previous, {}):
                    if previous not in residual_graph:
                        residual_graph[previous] = {}
                    residual_graph[previous][current] = 0
                residual_graph[current][previous] = residual_graph.get(current, {}).get(previous, 0) + path_flow
                
                current = previous
                
        return max_flow
        
    def find_augmenting_path(self, graph, source, sink):
        queue = deque([(source, [source], float('inf'))])
        visited = {source}
        
        while queue:
            node, path, flow = queue.popleft()
            
            for neighbor, capacity in graph.get(node, {}).items():
                if capacity > 0 and neighbor not in visited:
                    new_flow = min(flow, capacity)
                    new_path = path + [neighbor]
                    
                    if neighbor == sink:
                        return new_path, new_flow
                        
                    queue.append((neighbor, new_path, new_flow))
                    visited.add(neighbor)
                    
        return [], 0