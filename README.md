Improved Parallel Algorithm for Finding Minimum Cuts in Stochastic Flow Networks
Code and Resources for the Manuscript
This repository contains all the scripts and datasets required to reproduce the tables and figures presented in the manuscript "Efficient Minimum Cut Detection in Stochastic Networks". The work focuses on developing and evaluating a Dynamic Parallel Graph Cutting Algorithm, along with comparative analyses against traditional algorithms.

Repository Structure
1. Dataset and Experimental Data
The datasets used in the experiments are located in the Dataset/ folder. This includes:

Graph Instances: A collection of generated stochastic network graphs used in benchmarking.
Experimental Results: Precomputed outputs for different algorithms in .csv format, used for verification and reproducibility.
2. Code for Experiments
The implementation of the algorithms and related scripts are organized as follows:

Preprocessing (Preprocessing/)

Scripts for processing input graphs and formatting them for algorithmic evaluation.
File: preprocess.py
Algorithm Implementations (Algorithms/)

Dynamic Parallel Graph Cutting Algorithm (DPGCA/)
The main proposed method for efficient minimum cut detection.
File: dynamic_parallel_cut.py
Baseline Algorithms (Baselines/)
Implementations of Ford-Fulkerson, Edmonds-Karp, Push-Relabel, Stoer-Wagner, Karger, and Karger-Stein for comparative analysis.
Files: ford_fulkerson.py, edmonds_karp.py, etc.
Experimental Evaluation (Experiments/)

Scripts to run benchmarks and generate performance metrics.
File: run_experiments.py
3. Reproducing the Results
To reproduce the results from the paper, follow these steps:

Clone this repository:
bash
Copy
Edit
git clone https://github.com/yourusername/mincut-experiments.git
cd mincut-experiments
Set up the environment:
bash
Copy
Edit
pip install -r requirements.txt
Run the preprocessing step:
bash
Copy
Edit
python preprocess.py
Run experiments for a specific algorithm:
bash
Copy
Edit
python run_experiments.py --algorithm dynamic_parallel_cut
Analyze results and generate figures:
bash
Copy
Edit
python generate_figures.py
Citation
If you use this work, please cite the following publication:

pgsql
Copy
Edit
@article{mohammad2024,
  title={Improved Parallel Algorithm for Finding Minimum Cuts in Stochastic Flow Networks},
  author={Mohammad, joshan},
  journal={[IEEE Latin America]},
  year={2024},
}
Contact
For any questions or collaborations, please contact: mohammad@estudante.ufscar.br
