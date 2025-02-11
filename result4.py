import matplotlib.pyplot as plt

# Define graph sizes
graph_sizes = ["Small (500 nodes)", "Medium (50,000 nodes)", "Large (1,000,000 nodes)"]

# Hypothetical energy consumption in Joules (lower is better)
energy_ford_fulkerson = [500, 12000, 300000]
energy_edmonds_karp = [600, 15000, 400000]
energy_push_relabel = [400, 9000, 250000]
energy_karger = [350, 7500, 200000]
energy_dynamic_parallel_bk = [250, 5000, 150000]  # Proposed algorithm (best performance)

# Initialize the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Energy Consumption for Different Algorithms
ax.plot(graph_sizes, energy_ford_fulkerson, label='Parallel Ford-Fulkerson', marker='o', color='blue', linewidth=2)
ax.plot(graph_sizes, energy_edmonds_karp, label='Parallel Edmonds-Karp', marker='s', color='green', linewidth=2)
ax.plot(graph_sizes, energy_push_relabel, label='Parallel Push-Relabel', marker='^', color='purple', linewidth=2)
ax.plot(graph_sizes, energy_karger, label='Parallel Karger', marker='D', color='orange', linewidth=2)
ax.plot(graph_sizes, energy_dynamic_parallel_bk, label='Dynamic Parallel BK (Proposed)', marker='x', color='red', linewidth=2, linestyle='--')

# Set logarithmic scale for better visualization
ax.set_yscale('log')

# Set bold labels and title
ax.set_xlabel("Graph Size", fontsize=20, fontweight='bold')
ax.set_ylabel("Energy Consumption (Joules)", fontsize=20, fontweight='bold')


# Customize the legend
ax.legend(fontsize=16, title="Algorithms", title_fontsize=16, loc="upper left", frameon=True)

# Customize grid and tick labels
ax.grid(True, linestyle='--', linewidth=1.0)
ax.tick_params(axis='both', which='major', labelsize=16)

# Show the plot
plt.tight_layout()
plt.show()
