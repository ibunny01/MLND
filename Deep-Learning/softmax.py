"""Softmax."""

import numpy as np

scores = np.array([3.0, 1.0, 0.2])

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    # TODO: Compute and return softmax(x)

    exp_x = np.exp(x)
    return exp_x / np.sum( exp_x , axis=0 )

print(softmax(scores ))

print(softmax( scores * 10))

print(softmax( scores / 10))
