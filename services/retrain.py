import subprocess

def retrain():
    subprocess.run(["python", "model/train.py"])