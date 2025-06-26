import gc
import os
import time
from typing import Dict, List

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import psutil

from graph import Graph
from algorithms.ford_fulkerson import FordFulkerson
from algorithms.edmonds_karp import EdmondsKarp
from algorithms.push_relabel import PushRelabel
from algorithms.kargers_algorithm import KargersAlgorithm
from algorithms.bk_algorithm import BKAlgorithm
from algorithms.proposed_algorithm import ProposedAlgorithm

def benchmark_algorithms(graph_sizes: List[int], num_trials: int = 3):
    """Benchmark different algorithms on various graph sizes"""
    algorithms = {
        "Ford-Fulkerson": FordFulkerson(),
        "Edmonds-Karp": EdmondsKarp(),
        "Push-Relabel": PushRelabel(),
        "Karger's Algorithm": KargersAlgorithm(),
        "BK Algorithm": BKAlgorithm(),
        "Proposed Algorithm": ProposedAlgorithm()
    }
    
    results = {alg: {size: [] for size in graph_sizes} for alg in algorithms}
    memory_usage = {alg: {size: [] for size in graph_sizes} for alg in algorithms}
    
    for size in graph_sizes:
        print(f"\nTesting graph size: {size}")
        for trial in range(num_trials):
            print(f"  Trial {trial+1}/{num_trials}")
            graph = Graph(size).graph
            source, sink = 0, size - 1
            
            for alg_name, algorithm in algorithms.items():
                try:
                    process = psutil.Process(os.getpid())

                    gc.collect() # Force garbage collection before measurement
                    start_time = time.time()
                    before_mem = process.memory_info().rss / (1024 * 1024)  # MB
                    
                    max_flow = algorithm.max_flow(graph, source, sink)

                    after_mem = process.memory_info().rss / (1024 * 1024)  # MB
                    gc.collect()  # Force GC after as well
                    elapsed = (time.time() - start_time) * 1000  # Convert to milliseconds
                    
                    results[alg_name][size].append(elapsed)
                    mem = max(after_mem - before_mem, 0)  # Ensure memory usage is non-negative
                    memory_usage[alg_name][size].append(mem)
                    
                    print(f"    {alg_name}: {elapsed:.2f}ms, Flow: {max_flow}, Mem: {mem:.2f}MB")
                except Exception as e:
                    print(f"    {alg_name}: Error - {str(e)}")
                    # Use a default high value for errors
                    results[alg_name][size].append(float('inf'))
                    memory_usage[alg_name][size].append(0)
    
    return results, memory_usage

def create_table(results: Dict, graph_sizes: List[int]):
    """Create a table similar to the reference table"""
    data = []
    algorithms = list(results.keys())
    
    for alg in algorithms:
        row = [alg]
        for size in graph_sizes:
            avg_time = np.mean(results[alg][size])
            # Handle infinity
            if np.isinf(avg_time):
                avg_time = "Error"
            else:
                avg_time = f"{avg_time:.2f}"
            row.append(avg_time)
        data.append(row)
    
    columns = ["Algorithm"] + [f"Graph {i+1} (n={size})" for i, size in enumerate(graph_sizes)]
    df = pd.DataFrame(data, columns=columns)
    
    return df

def plot_results(results: Dict, memory_usage: Dict, graph_sizes: List[int]):
    """Generate performance comparison plots"""
    plt.figure(figsize=(16, 8))
    
    # Execution time plot
    plt.subplot(1, 2, 1)
    
    for alg_name in results:
        avg_times = []
        for size in graph_sizes:
            times = [t for t in results[alg_name][size] if not np.isinf(t)]
            if times:
                avg_times.append(np.mean(times))
            else:
                avg_times.append(np.nan)  # Use NaN for error cases
        plt.plot(graph_sizes, avg_times, marker='o', label=alg_name)
    
    plt.xlabel('Graph Size (nodes)')
    plt.ylabel('Execution Time (ms)')
    plt.title('Execution Time Comparison')
    plt.legend()
    plt.grid(True)
    
    # Memory usage plot
    plt.subplot(1, 2, 2)
    for alg_name in memory_usage:
        avg_mem = []
        for size in graph_sizes:
            mem_values = [m for m, t in zip(memory_usage[alg_name][size], results[alg_name][size]) if not np.isinf(t)]
            if mem_values:
                avg_mem.append(np.mean(mem_values))
            else:
                avg_mem.append(np.nan)
        plt.plot(graph_sizes, avg_mem, marker='o', label=alg_name)
    
    plt.xlabel('Graph Size (nodes)')
    plt.ylabel('Memory Usage (MB)')
    plt.title('Memory Consumption Comparison')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('algorithm_performance_comparison.png')
    plt.show()

def main():
    """Main function to run the benchmark and display results"""
    # Define graph sizes that approximately match the reference table
    # These sizes are chosen to produce execution times in the same range
    graph_sizes = [100, 300, 500]  # Adjust based on your hardware

    print("Running benchmark tests...")
    results, memory_usage = benchmark_algorithms(graph_sizes, num_trials=2)

    print("\nGenerating result table...")
    df_results = create_table(results, graph_sizes)
    print(df_results.to_string(index=False))

    print("\nGenerating performance plots...")
    plot_results(results, memory_usage, graph_sizes)

if __name__ == "__main__":
    main()
