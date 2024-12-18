import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data for the algorithms based on the summary table
algorithms = ["Ford-Fulkerson", "Edmonds-Karp", "Push-Relabel", "Parallel BK"]
execution_time = [3, 2, 2, 1]  # Scaled values where lower is better
memory_usage = [2, 3, 3, 1]    # Scaled values where lower is better
scalability = [1, 2, 3, 4]     # Scaled values where higher is better

# Set Seaborn style for better aesthetics
sns.set(style="whitegrid")

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Execution Time Plot
axs[0].barh(algorithms, execution_time, color='skyblue')
axs[0].set_title('Execution Time Comparison')
axs[0].set_xlabel('Execution Time (Lower is Better)')

# Memory Usage Plot
axs[1].barh(algorithms, memory_usage, color='salmon')
axs[1].set_title('Memory Usage Comparison')
axs[1].set_xlabel('Memory Usage (Lower is Better)')

# Scalability Plot
axs[2].barh(algorithms, scalability, color='lightgreen')
axs[2].set_title('Scalability Comparison')
axs[2].set_xlabel('Scalability (Higher is Better)')

plt.tight_layout()
plt.show()
