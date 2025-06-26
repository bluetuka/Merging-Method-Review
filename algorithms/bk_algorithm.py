from collections import deque
from typing import Dict

class BKAlgorithm:
    #def __init__(self, graph: Dict[int, Dict[int, int]], source: int, sink: int):
    def __init__(self):
        #self.graph = graph
        #self.source = source
        #self.sink = sink
        #self.residual_graph = self._init_residual_graph(graph)
        self.parent = {}
        self.tree_label = {}  # node -> 'S' (source tree) or 'T' (sink tree)

    def _init_residual_graph(self, graph: Dict[int, Dict[int, int]]) -> Dict[int, Dict[int, int]]:
        residual = {u: {} for u in graph}
        for u in graph:
            for v in graph[u]:
                residual[u][v] = graph[u][v]
                if v not in residual:
                    residual[v] = {}
                if u not in residual[v]:
                    residual[v][u] = 0
        return residual

    def _bfs_grow(self):# -> Optional[int]:
        """
        Grow source and sink trees using BFS.
        Return the meeting node if an augmenting path is found.
        """
        queue = deque()
        self.tree_label = {self.source: 'S', self.sink: 'T'}
        self.parent = {self.source: None, self.sink: None}
        queue.append(self.source)
        queue.append(self.sink)

        while queue:
            u = queue.popleft()
            tree = self.tree_label[u]
            for v in self.residual_graph[u]:
                if self.residual_graph[u][v] > 0:
                    if v not in self.tree_label:
                        self.tree_label[v] = tree
                        self.parent[v] = u
                        queue.append(v)
                    elif self.tree_label[v] != tree:
                        # Augmenting path found
                        self.parent[v] = u
                        return v  # Meeting point
        return None

    def _construct_path(self, meeting_point: int): # -> (list, int):
        """
        Construct path from source to sink through the meeting point.
        Return the path and its bottleneck capacity.
        """
        path = []
        flow = float('inf')

        # From meeting point to source
        u = meeting_point
        while u != self.source:
            prev = self.parent[u]
            flow = min(flow, self.residual_graph[prev][u])
            path.append((prev, u))
            u = prev

        path = list(reversed(path))

        # From meeting point to sink
        u = meeting_point
        while u != self.sink:
            next_node = None
            for v in self.residual_graph[u]:
                if self.tree_label.get(v) == 'T' and self.parent.get(v) == u:
                    next_node = v
                    break
            if next_node is None:
                break
            flow = min(flow, self.residual_graph[u][next_node])
            path.append((u, next_node))
            u = next_node

        return path, flow

    def _augment_path(self, path: list, flow: int):
        """
        Apply the flow through the given path by updating the residual graph.
        """
        for u, v in path:
            self.residual_graph[u][v] -= flow
            self.residual_graph[v][u] += flow

    def max_flow(self, graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
        """
        Run the BK-style algorithm and return the max flow.
        """
        self.graph = graph
        self.source = source
        self.sink = sink
        self.residual_graph = self._init_residual_graph(graph)

        total_flow = 0

        while True:
            meeting_point = self._bfs_grow()
            if not meeting_point:
                break

            path, flow = self._construct_path(meeting_point)
            self._augment_path(path, flow)
            total_flow += flow

        return total_flow