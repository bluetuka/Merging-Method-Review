import networkx as nx
import random

def generate_random_graph(num_nodes, edge_prob):
    """Generate a random directed graph with capacities."""
    G = nx.gnp_random_graph(num_nodes, edge_prob, directed=True)
    for u, v in G.edges():
        G[u][v]['capacity'] = random.randint(1, 10)
    return G

def partition_graph(graph, num_partitions=2):
    """Partition the graph into subgraphs."""
    nodes = list(graph.nodes())
    random.shuffle(nodes)
    partitions = [nodes[i::num_partitions] for i in range(num_partitions)]
    
    subgraphs = []
    for part in partitions:
        subgraph = graph.subgraph(part).copy()
        subgraphs.append(subgraph)
    
    return subgraphs

def check_edge_capacity_invariance(original_graph, modified_graph):
    """Check if edge capacities are preserved between two graphs."""
    for u, v in original_graph.edges():
        if modified_graph.has_edge(u, v):
            if original_graph[u][v]['capacity'] != modified_graph[u][v]['capacity']:
                print(f"Edge ({u}, {v}) capacity changed: {original_graph[u][v]['capacity']} -> {modified_graph[u][v]['capacity']}")
                return False
    return True

def merge_subgraphs(subgraphs, original_graph):
    """Merge the subgraphs while preserving edge capacities."""
    merged_graph = nx.compose_all(subgraphs)
    
    # Add edges between subgraphs from the original graph
    for u, v, data in original_graph.edges(data=True):
        if merged_graph.has_node(u) and merged_graph.has_node(v):
            if not merged_graph.has_edge(u, v):
                merged_graph.add_edge(u, v, capacity=data.get('capacity', 1))
    
    return merged_graph

def invariance_analysis(graph):
    """Conduct invariance analysis on the graph during processing."""
    print("\n--- Original Graph ---")
    for u, v, data in graph.edges(data=True):
        print(f"({u}, {v}) - Capacity: {data['capacity']}")

    # Step 1: Partition the graph
    subgraphs = partition_graph(graph, num_partitions=2)
    print("\n--- Subgraphs ---")
    for i, sg in enumerate(subgraphs):
        print(f"Subgraph {i + 1}: Nodes: {sg.nodes()}")

    # Step 2: Merge the subgraphs
    merged_graph = merge_subgraphs(subgraphs, graph)
    print("\n--- Merged Graph ---")
    for u, v, data in merged_graph.edges(data=True):
        print(f"({u}, {v}) - Capacity: {data['capacity']}")

    # Step 3: Check Edge Capacity Invariance
    is_invariant = check_edge_capacity_invariance(graph, merged_graph)
    if is_invariant:
        print("\nInvariance Check Passed: Edge capacities are preserved.")
    else:
        print("\nInvariance Check Failed: Edge capacities changed.")

# Example Workflow
def main():
    num_nodes = 10
    edge_prob = 0.3
    G = generate_random_graph(num_nodes, edge_prob)
    invariance_analysis(G)

if __name__ == "__main__":
    main()
