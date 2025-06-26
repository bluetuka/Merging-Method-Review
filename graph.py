import random
from typing import Dict

class Graph:
    def __init__(self, num_nodes: int, density: float = 0.3):
        self.num_nodes = num_nodes
        self.graph = self._generate_random_graph(density)
        
    def _generate_random_graph(self, density: float) -> Dict[int, Dict[int, int]]:
        """Generate a random flow network graph with given density"""
        graph = {i: {} for i in range(self.num_nodes)}
        
        for u in range(self.num_nodes):
            for v in range(u + 1, self.num_nodes):
                if random.random() < density:
                    capacity = random.randint(1, 100)
                    graph[u][v] = capacity
                    graph[v][u] = capacity  # Undirected graph
                    
        # Ensure the graph is connected
        for i in range(1, self.num_nodes):
            if not graph[0].get(i, False):
                capacity = random.randint(1, 100)
                graph[0][i] = capacity
                graph[i][0] = capacity
                
        return graph
