ACCURACY_THRESHOLD = 0.75

def check_model_health(acc, drift):
    if acc < ACCURACY_THRESHOLD or drift:
        return True
    return False