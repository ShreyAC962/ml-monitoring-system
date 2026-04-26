import subprocess
# Import subprocess module to run external commands/scripts

def retrain_model():
    # This executes: python model/train.py
    print("Retraining model...")
    subprocess.run(["python", "model/train.py"])