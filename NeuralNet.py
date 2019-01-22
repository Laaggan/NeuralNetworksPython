import numpy as np

class NeuralNet:
    #Here layerStructure should be a list of the number of inputs, neurons and outputs in each layer.
    def __init__(self, layerStructure):
        self.layerStructure = layerStructure
        self.weights = []
        self.thresholds = []
        self.localFields = []
        self.neurons = []
        self.InitializeWeightsAndThresholds()

    def InitializeWeightsAndThresholds(self):
        for i in range(1, self.layerStructure.__len__()):
            sigma = 1
            # initializing weight for a certain layer
            rows = self.layerStructure[i-1]
            cols = self.layerStructure[i]

            temp = np.random.normal(0, sigma, [rows, cols])
            temp = np.asmatrix(temp)
            self.weights.append(temp)

            # Initializing thresholds for the same layer
            temp = np.zeros([i, 1])
            self.thresholds.append(temp)
            self.localFields.append(temp)
            self.neurons.append(temp)

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def FeedForward(self, input):
        #FIXME: Error handling for if given input is not of same size as in self.layerStructure
        #if input.__len__() != self.layerStructure[0]:

        for i in range(self.weights.__len__()):
            #Perform matrix multiplication and add thresholds to obtain the local fields
            if i == 0:
                temp = np.add(np.matmul(input, self.weights[i]), self.thresholds[i])
                self.localFields.append(temp)
            else:
                temp = np.matmul(self.localFields[i-1], self.weights[i])
                self.localFields.append(temp)

            #Perform activation function on the local fields
            temp = np.zeros(self.localFields[i].shape)
            #FIXME: Do this without for-loop, temp = self.sigmoid(self.localFields[i], might work?
            for j in range(self.localFields[i].__len__()):
                temp[j] = self.sigmoid(self.localFields[i][j])
            self.neurons[i] = temp
