from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Adjacency list with capacities
        self.V = vertices  # Number of vertices

    def add_edge(self, u, v, capacity):
        """Adds an edge to the graph with a capacity."""
        self.graph[u].append((v, capacity))
    
    def bfs(self, source, sink, parent):
        """BFS to find an augmenting path and build the parent array."""
        visited = [False] * self.V
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)

            for v, capacity in self.graph[u]:
                if visited[v] == False and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def edmonds_karp(self, source, sink):
        """Edmonds-Karp algorithm to compute max flow."""
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            while s != source:
                u = parent[s]
                for v, capacity in self.graph[u]:
                    if v == s:
                        path_flow = min(path_flow, capacity)
                s = parent[s]

            v = sink
            while v != source:
                u = parent[v]
                for i, (v_adj, capacity) in enumerate(self.graph[u]):
                    if v_adj == v:
                        self.graph[u][i] = (v_adj, capacity - path_flow)
                for i, (u_adj, capacity) in enumerate(self.graph[v]):
                    if u_adj == u:
                        self.graph[v][i] = (u_adj, capacity + path_flow)
                        break
                else:
                    self.graph[v].append((u, path_flow))

                v = parent[v]

            max_flow += path_flow

        return max_flow

    def min_cut(self, source, sink):
        """Find the minimum cut by calculating the max flow first."""
        max_flow = self.edmonds_karp(source, sink)
        print(f"Maximum flow: {max_flow}")

        visited = [False] * self.V
        self.bfs(source, sink, visited)

        print("Min Cut Edges:")
        for u in range(self.V):
            if visited[u]:
                for v, capacity in self.graph[u]:
                    if not visited[v] and capacity == 0:  # Saturated edges
                        print(f"{u} - {v}")

    def merge_subgraph_flows(self, subgraphs):
        """Merging Method to combine flows from multiple subgraphs."""
        merged_flow = 0
        merged_cut_edges = []
        
        for subgraph in subgraphs:
            sub_max_flow = subgraph['max_flow']
            sub_cut_edges = subgraph['cut_edges']
            
            # Combine the flows
            merged_flow += sub_max_flow
            
            # Combine cut edges
            merged_cut_edges.extend(sub_cut_edges)
        
        return merged_flow, merged_cut_edges

    def partition_graph(self):
        """Partition the graph into two subgraphs for parallel processing."""
        mid = self.V // 2
        subgraph1 = Graph(mid)
        subgraph2 = Graph(self.V - mid)

        # Add edges to subgraphs manually for now (you can automate it)
        for u in range(mid):
            for v, cap in self.graph[u]:
                if v < mid:
                    subgraph1.add_edge(u, v, cap)
                else:
                    subgraph2.add_edge(u - mid, v - mid, cap)

        return subgraph1, subgraph2

    def min_cut_parallel(self, source, sink):
        """Parallel Min Cut using the Merging Method."""
        # Partition the graph into two subgraphs
        subgraph1, subgraph2 = self.partition_graph()

        # Compute max flow and min cut on each subgraph
        subgraph1_flow = subgraph1.edmonds_karp(source, subgraph1.V - 1)
        subgraph1_cut = [(u, v) for u in range(subgraph1.V) for v, cap in subgraph1.graph[u] if cap == 0]

        subgraph2_flow = subgraph2.edmonds_karp(0, subgraph2.V - 1)
        subgraph2_cut = [(u + subgraph1.V, v + subgraph1.V) for u in range(subgraph2.V) for v, cap in subgraph2.graph[u] if cap == 0]

        # Merging Method: Merge flows and cuts
        merged_flow, merged_cut_edges = self.merge_subgraph_flows([
            {'max_flow': subgraph1_flow, 'cut_edges': subgraph1_cut},
            {'max_flow': subgraph2_flow, 'cut_edges': subgraph2_cut}
        ])

        print(f"Total merged flow: {merged_flow}")
        print("Merged Min Cut Edges:")
        for edge in merged_cut_edges:
            print(f"{edge[0]} - {edge[1]}")

# Example usage:
g = Graph(6)
g.add_edge(0, 1, 16)
g.add_edge(0, 2, 13)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 12)
g.add_edge(2, 1, 4)
g.add_edge(2, 4, 14)
g.add_edge(3, 2, 9)
g.add_edge(3, 5, 20)
g.add_edge(4, 3, 7)
g.add_edge(4, 5, 4)

# Test parallel min cut
g.min_cut_parallel(0, 5)
