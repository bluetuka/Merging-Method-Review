import networkx as nx
import pandas as pd
import os

def load_graph(graph_path):
    """Loads a graph from a file, supporting different formats."""
    ext = os.path.splitext(graph_path)[1].lower()
    
    if ext == ".txt":
        return nx.read_edgelist(graph_path, nodetype=int, data=(('weight', float),))
    elif ext == ".csv":
        df = pd.read_csv(graph_path)
        graph = nx.from_pandas_edgelist(df, 'source', 'target', ['weight'])
        return graph
    elif ext == ".gml":
        return nx.read_gml(graph_path)
    else:
        raise ValueError("Unsupported file format. Use .txt, .csv, or .gml.")

def normalize_weights(graph):
    """Normalizes edge weights to be in the range [0,1]."""
    max_weight = max((d['weight'] for u, v, d in graph.edges(data=True)), default=1)
    for u, v, d in graph.edges(data=True):
        d['weight'] /= max_weight
    return graph

def preprocess_graph(graph):
    """Preprocesses the graph: normalization, MST, removes isolated nodes."""
    graph = normalize_weights(graph)
    
    # Ensuring connectivity using Minimum Spanning Tree (MST)
    mst = nx.minimum_spanning_tree(graph)
    
    # Removing isolated nodes
    nodes_to_remove = [node for node in mst.nodes if mst.degree(node) == 0]
    mst.remove_nodes_from(nodes_to_remove)
    
    return mst

if __name__ == "__main__":
    input_path = "Dataset/graph_instances.txt"  # Update if needed
    output_path = "Dataset/preprocessed_graph.gml"
    
    print("Loading graph...")
    graph = load_graph(input_path)
    
    print("Preprocessing graph...")
    processed_graph = preprocess_graph(graph)
    
    print("Saving preprocessed graph...")
    nx.write_gml(processed_graph, output_path)
    print(f"Preprocessed graph saved to {output_path}")

 