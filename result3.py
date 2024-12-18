import matplotlib.pyplot as plt

# Define hypothetical data for graph sizes
graph_sizes = ["Small (500 nodes)", "Medium (50,000 nodes)", "Large (1,000,000 nodes)"]

# Hypothetical execution times in seconds (parallel, reliability-focused)
exec_times_parallel_ford_fulkerson = [0.8, 10, 2000]
exec_times_parallel_edmonds_karp = [1.5, 30, 5000]
exec_times_parallel_push_relabel = [1, 8, 150]
exec_times_parallel_karger = [0.6, 5, 500]
exec_times_parallel_bk = [0.4, 3, 300]

# Hypothetical memory usage in MB (parallel, reliability-focused)
memory_usage_reliable_ford_fulkerson = [60, 1200, 24000]
memory_usage_reliable_edmonds_karp = [70, 1800, 35000]
memory_usage_reliable_push_relabel = [50, 800, 20000]
memory_usage_reliable_karger = [35, 700, 13000]
memory_usage_reliable_parallel_bk = [30, 600, 9000]

# Initialize the plot with subplots for Execution Time and Memory Usage
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot Execution Time with Reliability Constraints
ax1.plot(graph_sizes, exec_times_parallel_ford_fulkerson, label='Parallel Ford-Fulkerson', marker='o', color='blue')
ax1.plot(graph_sizes, exec_times_parallel_edmonds_karp, label='Parallel Edmonds-Karp', marker='s', color='green')
ax1.plot(graph_sizes, exec_times_parallel_push_relabel, label='Parallel Push-Relabel', marker='^', color='purple')
ax1.plot(graph_sizes, exec_times_parallel_karger, label='Parallel Karger', marker='D', color='orange')
ax1.plot(graph_sizes, exec_times_parallel_bk, label='Parallel BK', marker='x', color='red')

ax1.set_yscale('log')
ax1.set_xlabel("Graph Size")
ax1.set_ylabel("Execution Time (s)")
ax1.set_title("Parallel Execution Time with Reliability Constraints")
ax1.legend()
ax1.grid(True)

# Plot Memory Usage with Reliability Constraints
ax2.plot(graph_sizes, memory_usage_reliable_ford_fulkerson, label='Parallel Ford-Fulkerson', marker='o', color='blue')
ax2.plot(graph_sizes, memory_usage_reliable_edmonds_karp, label='Parallel Edmonds-Karp', marker='s', color='green')
ax2.plot(graph_sizes, memory_usage_reliable_push_relabel, label='Parallel Push-Relabel', marker='^', color='purple')
ax2.plot(graph_sizes, memory_usage_reliable_karger, label='Parallel Karger', marker='D', color='orange')
ax2.plot(graph_sizes, memory_usage_reliable_parallel_bk, label='Parallel BK', marker='x', color='red')

ax2.set_yscale('log')
ax2.set_xlabel("Graph Size")
ax2.set_ylabel("Memory Usage (MB)")
ax2.set_title("Memory Usage with Reliability Constraints in Parallel Processing")
ax2.legend()
ax2.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
