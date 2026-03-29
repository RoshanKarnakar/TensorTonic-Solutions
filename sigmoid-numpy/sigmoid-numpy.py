import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x)
    #Write code here
    f_x = 1 / (1 + np.exp(-x))
    return f_x
    