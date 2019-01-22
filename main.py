import numpy as np
import matplotlib.pyplot as plt
from NeuralNet import *

myNN = NeuralNet([2, 3, 1])

x = np.linspace(-10, 10)
y = myNN.sigmoid(x)


myNN