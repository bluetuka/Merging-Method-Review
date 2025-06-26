from typing import Dict

class PushRelabel:
    def max_flow(self, graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
        """Push-Relabel algorithm implementation"""
        # Initialize residual graph
        residual_graph = {u: {v: cap for v, cap in neighbors.items()} 
                         for u, neighbors in graph.items()}
        
        # Add reverse edges with 0 capacity if they don't exist
        for u in residual_graph:
            for v in list(residual_graph[u].keys()):
                if u not in residual_graph.get(v, {}):
                    if v not in residual_graph:
                        residual_graph[v] = {}
                    residual_graph[v][u] = 0
                    
        # Initialize height and excess flow
        height = {node: 0 for node in residual_graph}
        excess = {node: 0 for node in residual_graph}
        
        # Set source height to the number of nodes
        height[source] = len(residual_graph)
        
        # Push flow from source to its neighbors
        for v, cap in list(residual_graph[source].items()):
            residual_graph[source][v] = 0
            residual_graph[v][source] += cap
            excess[v] += cap
        
        # Main loop
        nodes = list(residual_graph.keys())
        nodes.remove(source)
        nodes.remove(sink)
        
        i = 0
        while i < len(nodes):
            u = nodes[i]
            
            if excess[u] > 0:
                # If there's excess flow, try to push or relabel
                pushed = False
                
                for v, cap in list(residual_graph[u].items()):
                    if cap > 0 and height[u] == height[v] + 1:
                        # Push operation
                        push_flow = min(excess[u], cap)
                        residual_graph[u][v] -= push_flow
                        residual_graph[v][u] += push_flow
                        excess[u] -= push_flow
                        excess[v] += push_flow
                        pushed = True
                        
                        if excess[u] == 0:
                            break
                
                if not pushed:
                    # Relabel operation
                    min_height = float('inf')
                    for v, cap in residual_graph[u].items():
                        if cap > 0:
                            min_height = min(min_height, height[v])
                    
                    if min_height != float('inf'):
                        height[u] = min_height + 1
                    
                    i = 0  # Start from the beginning after a relabel
                    continue
            
            i += 1
        
        # Return the excess flow at the sink as the max flow
        return excess[sink]