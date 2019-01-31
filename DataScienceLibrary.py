import numpy as np

#Takes a matrix x and the corresponding labels
#FIXME: maybe this should take a data frame instead of my data class
def MyKNN(newPoint, data, k):

    #Preallocate a vector to hold all distances to the new data point
    dataShape = data.x1.shape
    distances = np.zeros([dataShape[0]])

    #Calculate all distances to the new data point
    i = 0
    for x in zip(data.x1, data.x2):
        distances[i] = EuclideanDistance(x, newPoint)
        i += 1

    #Returns a list where the k first elements are guaranteed to be the index of the smallest elements
    idx = np.argpartition(distances, k)

    #Retrieve the label of the k smallest distances i.e. the k-Nearest Neighbours
    neighbours = data.labels[idx[0:k]]

    unique, counts = np.unique(neighbours, return_counts=True)
    winIdx = np.argmax(counts)

    return unique[winIdx]


def EuclideanDistance(x1, x2):
    #square root of the rowwise sum of the squared difference between the points
    distance = np.sqrt(np.sum((x1 - x2) ** 2))
    return distance
