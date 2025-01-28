Improved Parallel Algorithm for Finding Minimum Cuts in Stochastic Flow Networks
This repository contains the source code and datasets for the research article "Improved Parallel Algorithm for Finding Minimum Cuts in Stochastic Flow Networks" by Mohammad S. Joshan, José H. Saito, and Emerson C. Pedrino. The proposed algorithm optimizes the parallel Boykov-Kolmogorov (BK) algorithm to address convergence issues in large-scale stochastic flow networks (SFNs).

Overview
The study introduces a novel parallel framework and merging strategy for the BK algorithm, enabling:

30% reduction in execution time for large graphs.
40% reduction in memory usage.
Enhanced scalability and energy efficiency.
The algorithm was evaluated against existing methods (Ford-Fulkerson, Edmonds-Karp, Push-Relabel, Karger’s Algorithm) on a variety of graphs, ranging from small to large-scale networks.

Features
Implementation of the Dynamic Parallel Graph Cuts Algorithm.
Comparison with classical algorithms in terms of:
Execution time
Energy efficiency
Memory usage
Support for small, medium, and large graph datasets.
Repository Contents
src/: Source code implementing the algorithm in Python.
datasets/: Sample graph datasets (small, medium, and large scale).
results/: Precomputed results, including execution time and reliability analysis.
docs/: Supporting documentation and the original research article.
Requirements
Python 3.8+
Required libraries:
NumPy
NetworkX
Matplotlib (optional, for visualizations)
To install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Running the Code
Clone this repository:
bash
Copy
Edit
git clone https://github.com/your-repo-url.git
cd your-repo-url
Run the main script to execute the algorithm:
bash
Copy
Edit
python main.py --graph datasets/graph1.json --algorithm parallel
Use the --help flag for more options:
bash
Copy
Edit
python main.py --help
Results
Key findings from the study include:

The proposed algorithm achieves faster execution times compared to other methods, especially for large-scale graphs.
The results demonstrate low variance across multiple runs, confirming the reliability of the approach.
Detailed comparisons and statistical analyses are available in the published article.
Citation
If you use this code or data in your research, please cite our article:

bibtex
Copy
Edit
@article{joshan2025parallel,
  title={Improved Parallel Algorithm for Finding Minimum Cuts in Stochastic Flow Networks},
  author={Joshan, Mohammad Sadegh and Saito, José H. and Pedrino, Emerson C.},
  journal={Journal of LaTeX Class Files},
  volume={18},
  number={9},
  pages={1--7},
  year={2024}
}
License
This project is licensed under the MIT License.

Contact
For questions or feedback, feel free to contact the authors:

Mohammad S. Joshan: mohammad@estudante.ufscar.br
