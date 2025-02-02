Minimum Cuts in Stochastic Flow Networks
This repository provides all the necessary code and resources to reproduce the results presented in the manuscript:
"Efficient Minimum Cut Detection in Stochastic Networks."

The research introduces the Dynamic Parallel Graph Cutting Algorithm (DPGCA) and includes comparative analyses against traditional minimum cut algorithms.

📂 Repository Structure
1. Dataset and Experimental Data
Located in the Dataset/ folder, including:

Graph Instances: Stochastic network graphs used for benchmarking.
Experimental Results: Precomputed outputs in .csv format for verification and reproducibility.
2. Code for Experiments
Preprocessing (Preprocessing/)
Scripts for processing input graphs and preparing them for evaluation.

File: preprocess.py
Algorithm Implementations (Algorithms/)
Dynamic Parallel Graph Cutting Algorithm (DPGCA/)
The primary proposed method for efficient minimum cut detection.
File: dynamic_parallel_cut.py
Baseline Algorithms (Baselines/)
Implementations of Ford-Fulkerson, Edmonds-Karp, Push-Relabel, Stoer-Wagner, Karger, and Karger-Stein.
Files: ford_fulkerson.py, edmonds_karp.py, etc.
Graph Cutting Algorithms (C++ - Minimum Cut Algorithms/)
Contains implementations of:

Ford-Fulkerson
Edmonds-Karp
Push-Relabel
Karger’s Algorithm
BK Algorithm
Proposed Dynamic Parallel Graph Cutting Algorithm
3. Comparative Analysis and Visualization (Jupyter - Analysis/)
Jupyter Notebook scripts for:

Graph visualization
Performance comparison
Generating tables and figures from the paper
🚀 Getting Started
Clone the Repository
bash
Copy
Edit
git clone https://github.com/bluetuka/Merging-Method-Review
cd mincut-experiments
Run Experiments for a Specific Algorithm
bash
Copy
Edit
python run_experiments.py --algorithm dynamic_parallel_cut
Generate Figures and Analyze Results
bash
Copy
Edit
python generate_figures.py
🔗 Citation
If you use this repository, please cite:

bibtex
Copy
Edit
@article{mohammad2024,
  title={Improved Parallel Algorithm for Finding Minimum Cuts in Stochastic Flow Networks},
  author={Mohammad, Joshan},
  journal={IEEE Latin America},
  year={2024}
}
📧 Contact
For questions or collaborations, feel free to reach out:
📩 mohammad@estudante.ufscar.br

