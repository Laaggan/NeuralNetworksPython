import numpy as np
import matplotlib.pyplot as plt

# Create a random pattern
N = 20  # Number of neurons
n = 10  # Number of patterns
x = np.random.randint(2, size=[N, n]) # The 2 makes the range [0, 1]

print(x)