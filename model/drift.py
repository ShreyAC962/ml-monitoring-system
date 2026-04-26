import numpy as np

def detect_drift(old_data, new_data, threshold = 0.2):
    drift = np.abs(np.mean(old_data) - np.mean(new_data))
    return drift > threshold
