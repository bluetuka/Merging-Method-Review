# Code for Efficient Minimum Cut Detection in Stochastic Networks

Resources and extra documentation for the manuscript **"Efficient Minimum Cut Detection in Stochastic Networks"**. This repository contains all scripts required to reproduce the tables and figures presented in the paper.

## Code Organization
The code is organized by type of process:

- **Pre-processing**: Python
- **Graph Cutting Algorithms**: C++
- **Comparative Analysis and Visualization**: Jupyter Notebook

## Dataset and Subsets
The dataset files are located in the folder **"Dataset - Stochastic Flow Networks"**. Inside this folder, you will find:

- **Original dataset**: `StochasticFlowNetworkData.csv`
- **Subdivisions for K-fold cross-validation**: Found inside the "K-fold cross-validation" folder, categorized into `k = 2`, `k = 3`, `k = 4`, and `k = 5`. Each folder contains subsets labeled as `D1`, `D2`, `D3`, etc., in `.txt` format for easy integration into the code.

## Code Descriptions

### Pre-processing
The pre-processing scripts are located in the folder **"PYTHON - Pre-processing"**. These scripts handle:
- Data cleaning and transformation
- Feature extraction
- Graph representation generation

You only need to provide the dataset in CSV format as described above.

### Graph Cutting Algorithms
The core algorithm implementations are in the folder **"C++ - Minimum Cut Algorithms"**, which contains:
- **Ford-Fulkerson**
- **Edmonds-Karp**
- **Push-Relabel**
- **Karger’s Algorithm**
- **BK Algorithm**
- **Proposed Dynamic Parallel Graph Cutting Algorithm**

For each algorithm, the corresponding K-fold cross-validation divisions (`K=2`, `K=3`, `K=4`, `K=5`) are available. Each contains further divisions for training and testing, such as `D1 training - D2 testing`.

### Comparative Analysis and Visualization
The Jupyter Notebook scripts in **"Jupyter - Analysis"** facilitate:
- Graph plotting
- Comparative performance analysis
- Table and figure generation as presented in the paper

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

