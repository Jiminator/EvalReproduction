# Evaluation Reproduction Setup for CS598: How to do Research

Since recreating LLM pre-training experiments are quite hard and requires significant compute resources, we decided to bring the training logs from our runs on Megatron-DeepSpeed into this repository, and provide the code we used to parse the training logs, analyze the training speed using specific metrics, and to plot the training curves. We can choose to run the python [script](src/analyze.py)  which will store the plotted images in a directory called outputs. If you have ipykernel installed, you can also choose to use our provided [Jupyter Notebook](analyze.ipynb) to perform the data analysis. We also provided the Megatron-DeepSpeed shell [script](src/run_deepspeed.sh) used to pre-train the LLMs. This can copied into the [Megatron-DeepSpeed](https://github.com/microsoft/Megatron-DeepSpeed/blob/main/examples_deepspeed/run_deepspeed_example.sh) repo if an individual has the compute to recreate our results.

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
# If running script
python3 src/analyze.py
```

#### Supported Python Versions
- 3.11

## Training Configurations
#### Hardware
2 [c240g5](https://docs.cloudlab.us/hardware.html) Cloudlab nodes, each fitted with one P100 GPU

#### Full Pre-Training Configuration
Full pre-training hyperparameters and configuration can be found [here](src/run_deepspeed.sh).
Iterations: 1000
DP = 2, TP = 1, PP = 1


#### Ablation Study Configurations
Same configuration file as full pre-training but increase iterations, and change PP and TP values.
Iterations: 100
DP Only: DP = 2, TP = 1, PP = 1
TP Only: DP = 1, TP = 2, PP = 1
PP Only: DP = 1, TP = 1, PP = 2
