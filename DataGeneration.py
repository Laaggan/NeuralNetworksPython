import numpy as np
import matplotlib.pyplot as plt

class SimpleDataset:
    def __init__(self, numberOfPoints):
        # Number of generated data points
        n = numberOfPoints
        labels1 = np.ones([numberOfPoints, 1])
        labels2 = 2*np.ones([numberOfPoints, 1])
        self.labels = np.concatenate(labels1, labels2)

        # The parameters for the different clusters
        mu1 = 1
        mu2 = 4
        sigma1 = 0.5
        sigma2 = 1

        x1 = np.random.normal(mu1, sigma1, n)
        x2 = np.random.normal(mu2, sigma2, n)
        self.x = np.concatenate(x1, x2)

        y1 = np.random.normal(mu1, sigma1, n)
        y2 = np.random.normal(mu2, sigma2, n)
        self.y = np.concatenate(y1, y2)


#Number of generated data points
n = 100

#The parameters for the different clusters
mu1 = 1
mu2 = 4
sigma1 = 0.5
sigma2 = 1

x1 = np.random.normal(mu1, sigma1, n)
x2 = np.random.normal(mu2, sigma2, n)

y1 = np.random.normal(mu1, sigma1, n)
y2 = np.random.normal(mu2, sigma2, n)

data = SimpleDataset(100)

plt.scatter(data.x, data.y)
plt.show()