import numpy as np
from scipy.stats import ks_2samp
# Import Kolmogorov-Smirnov test for comparing two distributions

def detect_drift(old_data, new_data, threshold = 0.05):
    """
    Uses KS test (Kolmogorov-Smirnov) for real drift detection
    """
    old_data = np.array(old_data)
    new_data = np.array(new_data)

    # statistic → measures difference between distributions
    # p_value → probability that both datasets come from same distribution

    statistic, p_value = ks_2samp(old_data, new_data)

    print("Drift score:", statistic, "p-value:", p_value)

    return p_value < threshold
