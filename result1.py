import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Define synthetic data for demonstration
graph_sizes = ['Small (500 nodes)', 'Medium (50,000 nodes)', 'Large (1,000,000 nodes)']
execution_time = [2, 10, 30]  # Example values in seconds
memory_usage = [50, 250, 1000]  # Example values in MB
scalability = [1, 2, 3]  # Arbitrary units for comparison

# Set style and context for professional look
sns.set_theme(style="whitegrid", context="talk")

# Initialize the figure
fig, axes = plt.subplots(1, 3, figsize=(20, 6), sharey=False)

# Execution Time Plot
sns.barplot(x=graph_sizes, y=execution_time, palette="Blues_d", ax=axes[0])
axes[0].set_title("Execution Time Comparison", fontsize=16, fontweight='bold')
axes[0].set_xlabel("Graph Size", fontsize=12)
axes[0].set_ylabel("Time (s)", fontsize=12)
axes[0].tick_params(axis='x', rotation=15)

# Memory Usage Plot
sns.barplot(x=graph_sizes, y=memory_usage, palette="Greens_d", ax=axes[1])
axes[1].set_title("Memory Usage Comparison", fontsize=16, fontweight='bold')
axes[1].set_xlabel("Graph Size", fontsize=12)
axes[1].set_ylabel("Memory (MB)", fontsize=12)
axes[1].tick_params(axis='x', rotation=15)

# Scalability Plot
sns.barplot(x=graph_sizes, y=scalability, palette="Oranges_d", ax=axes[2])
axes[2].set_title("Scalability Comparison", fontsize=16, fontweight='bold')
axes[2].set_xlabel("Graph Size", fontsize=12)
axes[2].set_ylabel("Scalability (Units)", fontsize=12)
axes[2].tick_params(axis='x', rotation=15)

# Adjust layout for better spacing
plt.tight_layout()
plt.show()
