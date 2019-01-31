import numpy as np
import matplotlib.pyplot as plt
from NeuralNet import *
from DataGeneration import *
from DataScienceLibrary import *

myNN = NeuralNet([2, 3, 1])

x = np.linspace(-10, 10)
y = myNN.sigmoid(x)


myData = SimpleDataset(10)

newPoint = np.array([1, 1])
print(MyKNN(newPoint, myData, 3))