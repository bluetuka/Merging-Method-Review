# Code for Improved Parallel Algorithm for Finding Minimum Cuts in Stochastic Flow Networks

Resources and extra documentation for the manuscript **"Improved Parallel Algorithm for Finding Minimum Cuts in Stochastic Flow Networks"**. This repository contains all scripts required to reproduce the tables and figures presented in the paper.

## Code Organization
The code is organized by type of process:

- **Pre-processing**: Python
- **Comparative Analysis and Visualization**: Jupyter Notebook

## Code and Resources for the Manuscript

This repository contains all the scripts and datasets required to reproduce the tables and figures presented in the manuscript **"Efficient Minimum Cut Detection in Stochastic Networks"**. The work focuses on developing and evaluating a **Dynamic Parallel Graph Cutting Algorithm (DPGCA)** along with comparative analyses against traditional algorithms.

## Repository Structure

### 1. Dataset and Experimental Data
The datasets used in the experiments are located in the `Dataset/` folder, including:
- **Graph Instances**: A collection of generated stochastic network graphs used in benchmarking.
- **Experimental Results**: Precomputed outputs for different algorithms in `.csv` format, used for verification and reproducibility.
- 
### 2. Code for Experiments
The implementation of the algorithms and related scripts are organized as follows:

#### **Preprocessing (`Preprocessing/`):**
Scripts for processing input graphs and formatting them for algorithmic evaluation.
- **File**: `preprocess.py`

#### **Algorithm Implementations (`Algorithms/`):**
- **Dynamic Parallel Graph Cutting Algorithm (`DPGCA/`)**
  - The main proposed method for efficient minimum cut detection.
  - **File**: `dynamic_parallel_cut.py`
- **Baseline Algorithms (`Baselines/`)**
  - Implementations of Ford-Fulkerson, Edmonds-Karp, Push-Relabel, Stoer-Wagner, Karger, and Karger-Stein for comparative analysis.
  - **Files**: `ford_fulkerson.py`, `edmonds_karp.py`, etc.

### Graph Cutting Algorithms
The core algorithm implementations are in the folder **"C++ - Minimum Cut Algorithms"**, which contains:
- **Ford-Fulkerson**
- **Edmonds-Karp**
- **Push-Relabel**
- **Karger’s Algorithm**
- **BK Algorithm**
- **Proposed Dynamic Parallel Graph Cutting Algorithm**
## Code Descriptions
For each algorithm, the corresponding K-fold cross-validation divisions (`K=2`, `K=3`, `K=4`, `K=5`) are available. Each contains further divisions for training and testing, such as `D1 training - D2 testing`.

### Comparative Analysis and Visualization
The Jupyter Notebook scripts in **"Jupyter - Analysis"** facilitate:
- Graph plotting
- Comparative performance analysis
- Table and figure generation as presented in the paper

### Pre-processing
The pre-processing scripts are located in the folder **"PYTHON - Merging-Method"**. These scripts handle:
- Data cleaning and transformation
- Feature extraction
- Graph representation generation

You only need to provide the dataset in CSV format as described above.



## Notes
- The dataset is stored in a separate folder, but all C++ codes already have the respective dataset subdivisions placed in the training and testing sections for direct compilation.
- Scripts are well-commented to ensure reproducibility.

## Contact
For any inquiries or issues regarding the code, please contact the corresponding author of the paper.

---

**Repository Statistics**

- **Languages**: C++ (Primary), Python, Jupyter Notebook
- **Status**: Actively maintained

Thank you for using this repository. If you find it useful, consider citing our work!


### Clone this repository:
```bash
git clone https://github.com/bluetuka/Merging-Method-Review
cd mincut-experiments
```

### Run experiments for a specific algorithm:
```bash
python run_experiments.py --algorithm dynamic_parallel_cut
```

### Analyze results and generate figures:
```bash
python generate_figures.py
```

## Citation
If you use this work, please cite the following publication:
```bibtex
@article{mohammad2024,
  title={Improved Parallel Algorithm for Finding Minimum Cuts in Stochastic Flow Networks},
  author={Mohammad, Joshan},
  journal={[IEEE Latin America]},
  year={2024}
}
```

## Contact
For any questions or collaborations, please contact: mohammad@estudante.ufscar.br



