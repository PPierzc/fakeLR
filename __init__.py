import numpy as np

def predict(x):
    w = np.array([5, 1])
    phi = np.array([x, 1])
    prediction = w.T @ phi
    return prediction.item()