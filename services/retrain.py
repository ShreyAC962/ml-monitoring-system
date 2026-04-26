import subprocess
# Import subprocess module to run external commands/scripts

def retrain():
    # This executes: python model/train.py
    subprocess.run(["python", "model/train.py"])