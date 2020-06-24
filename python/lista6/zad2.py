import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork:
    def __init__(self, x, y, eta):
        self.input = x
        self.weights1 = np.random.rand(10, self.input.shape[1])
        self.weights2 = np.random.rand(1, 10)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = eta

    def tanh_feed_forward(self):
        self.layer1 = tanh(np.dot(self.input, self.weights1.T))
        self.output = tanh(np.dot(self.layer1, self.weights2.T))

    def tanh_back_prop(self):
        delta2 = (self.y - self.output) * tanh_der(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = tanh_der(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)
        self.weights1 += d_weights1
        self.weights2 += d_weights2


def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))


def tanh_der(x):
    return 1.0 - tanh(x) ** 2


def square_error(x, y):
    se = 0
    for i in zip(x, y):
        se += (i[0] - i[1]) ** 2
    return se / len(x)


if __name__ == '__main__':

    a = 10000
    step = 200
    print("Wybierz funkcję, której mam się nauczyć : ")
    inp = input("(s - sinus, p - parabola)")
    time = 0.1

    if inp == "p":
        n = 101
        r = 50
        X = np.linspace(start=-r, stop=r, num=n)
        X = X / r
        y = X ** 2
        z = X.reshape(n, 1)
        arr = [[1] for i in range(n)]
        z = np.hstack((z, np.array(arr)))
        z = np.hstack((z, np.array(arr)))
        line_y = y.reshape(n, 1)
        np.random.seed(17)
        nn = NeuralNetwork(z, line_y, 0.001)
        for steps in range(a):
            nn.tanh_feed_forward()
            nn.tanh_back_prop()
            if steps % step == 0:
                plt.scatter(X * r, nn.output * r ** 2)
                print("krok: ", step, "Błąd=  ", square_error(y, nn.output))
                plt.pause(time)
                plt.close()

    else:
        n = 161
        r = 2
        X = np.linspace(start=-r, stop=r, num=n)
        y = np.sin((3 * np.pi / 2) * X)
        X = X / r
        z = X.reshape(n, 1)
        arr = [[1] for i in range(n)]
        z = np.hstack((z, np.array(arr)))
        line_y = y.reshape(n, 1)
        np.random.seed(17)
        nn = NeuralNetwork(z, line_y, 0.001)
        for steps in range(a):
            nn.tanh_feed_forward()
            nn.tanh_back_prop()
            if steps % step == 0:
                plt.scatter(X * r, nn.output)
                print("krok: ", step, "Błąd =  ", square_error(y, nn.output))
                plt.pause(time)
                plt.close()

