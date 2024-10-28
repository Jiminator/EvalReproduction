# Evaluation Reproduction Setup for CS598: How to do Research

Since recreating LLM pre-training experiments are quite hard and requires significant compute resources, we decided to bring the training logs from our runs on DeepSpeed into this repository, and provide the code we used to parse the training logs, analyze the training speed using specific metrics, and to plot the training curves. We can choose to run the python [script](src/analyze.py)  which will store the plotted images in a directory called outputs. If you have ipykernel installed, you can also choose to use our provided [Jupyter Notebook](analyze.ipynb) to perform the data analysis.

## Install
To run this project, you need to install the required packages. Follow the steps below to install the dependencies using the [requirements.txt](requirements.txt) file.

1. Clone the repository: 
```bash
git clone https://github.com/Jiminator/EvalReproduction.git
```

2. Navigate to the project directory:
```bash 
cd EvalReproduction
```

3. Install dependencies using the requirements.txt file: 
```bash
# If using conda
conda create -n EvalReproduction python=3.11 pip -y
conda activate EvalReproduction

pip install -r requirements.txt
```

4. Once all dependencies are installed, you are ready to run the script and/or use the [Jupyter Notebook](analyze.ipynb). Training metric data will be displayed in the command line, whereas loss curves will stored in the outputs directory.
```bash
# If using running script
python3 src/analyze.py
```

#### Supported Python Versions
- 3.11
