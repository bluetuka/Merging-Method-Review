import random
from typing import Dict

import numpy as np

from algorithms.ford_fulkerson import FordFulkerson

class KargersAlgorithm:
    def min_cut(self, graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
        """Karger's randomized min-cut algorithm (simplified)"""
        # Number of repetitions to ensure high probability of finding min-cut
        repetitions = int(np.log(len(graph)) * len(graph))
        min_cut_value = float('inf')
        
        for _ in range(repetitions):
            # Create a copy of the graph
            graph_copy = {u: {v: cap for v, cap in neighbors.items()} 
                         for u, neighbors in graph.items()}
            
            # Run a single iteration of Karger's algorithm
            cut_value = self._karger_iteration(graph_copy, source, sink)
            min_cut_value = min(min_cut_value, cut_value)
            
        return min_cut_value
    
    def _karger_iteration(self, graph, source, sink):
        # Create a union-find data structure to track merged vertices
        parent = {node: node for node in graph}
        rank = {node: 0 for node in graph}
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            
            if root1 != root2:
                if rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    if rank[root1] == rank[root2]:
                        rank[root1] += 1
        
        # Create a list of all edges
        edges = []
        for u in graph:
            for v, cap in graph[u].items():
                if u < v:  # To avoid counting edges twice
                    edges.append((u, v, cap))
        
        # Contract edges until only two vertices remain
        num_vertices = len(graph)
        while num_vertices > 2:
            # Select a random edge
            if not edges:
                break
            edge_idx = random.randint(0, len(edges) - 1)
            u, v, _ = edges[edge_idx]
            
            # Contract the edge if it doesn't create a self-loop
            if find(u) != find(v):
                union(u, v)
                num_vertices -= 1
            
            # Remove the selected edge
            edges.pop(edge_idx)
        
        # Calculate the cut value
        cut_value = 0
        source_root = find(source)
        sink_root = find(sink)
        
        if source_root == sink_root:
            # If source and sink are in the same set, use a different approach
            ff = FordFulkerson()
            return ff.max_flow(graph, source, sink)
        
        # Calculate cut value by summing capacities of edges between the two sets
        for u in graph:
            for v, cap in graph[u].items():
                if find(u) != find(v):
                    cut_value += cap
        
        return cut_value
    
    def max_flow(self, graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
        """Max flow is equal to min cut value by max-flow min-cut theorem"""
        return self.min_cut(graph, source, sink)