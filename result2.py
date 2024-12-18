import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import networkx as nx
from matplotlib.colors import ListedColormap

# Set up seaborn style for professional visuals
sns.set(style="whitegrid")

# 1. Performance Under Varying Stochastic Conditions
def plot_performance_with_variability():
    algorithms = ['Ford-Fulkerson', 'Edmonds-Karp', 'Push-Relabel', 'Parallel BK']
    avg_times = [30, 20, 15, 8]  # Average execution times in seconds
    avg_memory = [120, 200, 300, 80]  # Average memory usage in MB
    scalability = [100, 200, 300, 500]  # Scalability in terms of nodes handled

    # Adding stochastic variability
    times = [np.random.normal(loc=t, scale=5, size=10) for t in avg_times]
    memory_usage = [np.random.normal(loc=m, scale=20, size=10) for m in avg_memory]
    scalability_variants = [np.random.normal(loc=s, scale=50, size=10) for s in scalability]

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # Execution Time with Variability
    sns.boxplot(data=times, ax=axes[0])
    axes[0].set_title("Execution Time under Stochastic Conditions")
    axes[0].set_xticklabels(algorithms)
    axes[0].set_ylabel("Time (seconds)")

    # Memory Usage with Variability
    sns.boxplot(data=memory_usage, ax=axes[1], palette="coolwarm")
    axes[1].set_title("Memory Usage under Stochastic Conditions")
    axes[1].set_xticklabels(algorithms)
    axes[1].set_ylabel("Memory Usage (MB)")

    # Scalability with Variability
    sns.boxplot(data=scalability_variants, ax=axes[2], palette="viridis")
    axes[2].set_title("Scalability under Stochastic Conditions")
    axes[2].set_xticklabels(algorithms)
    axes[2].set_ylabel("Scalability (Nodes)")

    plt.tight_layout()
    plt.show()

# 2. Visualization of Graph Structure and Execution Stages
def visualize_graph_execution():
    # Create a sample graph
    G = nx.erdos_renyi_graph(n=20, p=0.2, seed=42)
    
    # Define positions for nodes
    pos = nx.spring_layout(G, seed=42)
    
    # Draw initial state of the graph
    plt.figure(figsize=(10, 7))
    plt.title("Graph Structure - Initial State")
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
    plt.show()

    # Simulate mid-execution (highlight some edges/nodes)
    plt.figure(figsize=(10, 7))
    plt.title("Graph Structure - Mid Execution Stage")
    nx.draw(G, pos, with_labels=True, node_color="lightgreen", edge_color="gray", node_size=500, font_size=10)
    nx.draw_networkx_nodes(G, pos, nodelist=[0, 1, 2, 3], node_color="orange")  # Highlight some nodes
    nx.draw_networkx_edges(G, pos, edgelist=[(0, 1), (1, 2), (2, 3)], edge_color="red", width=2)  # Highlight some edges
    plt.show()

    # Final state visualization (completed algorithm)
    plt.figure(figsize=(10, 7))
    plt.title("Graph Structure - Final State (Algorithm Completion)")
    nx.draw(G, pos, with_labels=True, node_color="lightcoral", edge_color="blue", node_size=500, font_size=10)
    plt.show()

# Run both visualizations
plot_performance_with_variability()
visualize_graph_execution()
