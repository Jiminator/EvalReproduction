# Evaluation Reproduction Setup for CS598: How to do Research

Since recreating LLM pre-training experiments are quite hard and requires significant compute resources, we decided to bring the training logs from our runs on DeepSpeed into this repository, and provide the code we used to parse the training logs, analyze the training speed using specific metrics, and to plot the training curves.

## Install
To run this project, you need to install the required packages. Follow the steps below to install the dependencies using the requirements.txt file

1. Clone the repository: 
```bash
git clone https://github.com/SamsungLabs/Metis.git
```

2. Navigate to the project directory:
```bash 
cd ~/Metis
```

3. Install dependencies using the requirements.txt file: 
```bash
pip install -r requirements.txt
```

4. Once all dependencies are installed, you are ready to run the project.