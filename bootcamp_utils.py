# Bootcamp utils: A collection of statistical functions
import numpy as np

def ecdf(data):
    """
    Compute x, y values for an empirial dist. function
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / 1/len(x)

    return x, y
