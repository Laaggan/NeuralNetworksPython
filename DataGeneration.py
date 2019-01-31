import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SimpleDataset:
    def __init__(self, numberOfPoints):
        # Number of generated data points
        n = numberOfPoints
        labels1 = np.ones([numberOfPoints, 1])
        labels2 = 2*np.ones([numberOfPoints, 1])
        self.labels = np.concatenate([labels1, labels2])

        # The parameters for the different clusters
        mu1 = 1
        mu2 = 4
        sigma1 = 0.5
        sigma2 = 1

        x1 = np.random.normal(mu1, sigma1, n)
        x2 = np.random.normal(mu2, sigma2, n)
        self.x1 = np.concatenate([x1, x2])

        y1 = np.random.normal(mu1, sigma1, n)
        y2 = np.random.normal(mu2, sigma2, n)
        self.x2 = np.concatenate([y1, y2])

#FIXME: return a data frame instead of an object as in "class SimleDataset"
'''
def CreateDataFrame(numberOfPoints=100):
    colNames = np.array(['index', 'x', 'y'])
    indices = np.arange(numberOfPoints)

    # FIXME: make this non-static so you can make high-dimensional data
    # The parameters for the different clusters
    mu1 = 1
    mu2 = 4
    sigma1 = 0.5
    sigma2 = 1

    # Number of generated data points
    labels1 = np.ones(numberOfPoints)
    labels2 = 2*np.ones(numberOfPoints)
    labels = np.concatenate([labels1, labels2])

    x1 = np.random.normal(mu1, sigma1, numberOfPoints)
    x2 = np.random.normal(mu2, sigma2, numberOfPoints)
    x = np.concatenate([x1, x2])

    y1 = np.random.normal(mu1, sigma1, numberOfPoints)
    y2 = np.random.normal(mu2, sigma2, numberOfPoints)
    y = np.concatenate([y1, y2])

    data1 = np.array(['', 'x', 'y'],
                     [indices, x1, y1])

    #data1 = np.r_[colNames, data1]

    return data1
'''

'''
#Some lines of code to test the class
data = SimpleDataset(100)

plt.scatter(data.x1, data.x2)
plt.show()
'''