import numpy as np


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1.0 - x)


def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return 1. * (x > 0)


class NeuralNetwork:
    def __init__(self, x, y, activator1="sigmoid", activator2="sigmoid"):
        self.input = x

        self.activator1 = activator1
        self.activator2 = activator2
        if activator1 == "relu":
            np.random.seed(17)
        else:
            np.random.seed(3)
        self.weights1 = np.random.rand(4, self.input.shape[1])
        if activator2 == "relu":
            np.random.seed(17)
        else:
            np.random.seed(3)
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = 0.05
        self.layer1 = np.zeros(4)

    def feed_forward(self):
        if self.activator1 == "sigmoid":
            self.layer1 = sigmoid(np.dot(self.input, self.weights1.T))
        else:
            self.layer1 = relu(np.dot(self.input, self.weights1.T))
        if self.activator2 == "sigmoid":
            self.output = sigmoid(np.dot(self.layer1, self.weights2.T))
        else:
            self.output = relu(np.dot(self.layer1, self.weights2.T))

    def back_prop(self):
        if self.activator2 == "sigmoid":
            delta2 = (self.y - self.output) * sigmoid_derivative(self.output)
        else:
            delta2 = (self.y - self.output) * relu_derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)

        if self.activator1 == "sigmoid":
            delta1 = sigmoid_derivative(self.layer1) * np.dot(delta2,
                                                              self.weights2)
        else:
            delta1 = relu_derivative(self.layer1) * np.dot(delta2,
                                                           self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2

