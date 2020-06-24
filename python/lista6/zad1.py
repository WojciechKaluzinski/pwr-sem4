import neural_network
import numpy as np


def prepare_models(x, y):
    return [neural_network.NeuralNetwork(x, y, "sigmoid", "relu"),
            neural_network.NeuralNetwork(x, y, "relu", "relu"),
            neural_network.NeuralNetwork(x, y, "sigmoid", "sigmoid"),
            neural_network.NeuralNetwork(x, y, "relu", "sigmoid")
            ]


if __name__ == '__main__':
    """
        ostatnia kolumna to bias - służy do przesunięcia
        aktywacji neuronu
    """

    xor_networks = prepare_models(np.array([[0, 0, 1],
                                            [0, 1, 1],
                                            [1, 0, 1],
                                            [1, 1, 1]]),
                                  np.array([[0], [1], [1], [0]]))
    and_networks = prepare_models(np.array([[0, 0, 1],
                                            [0, 1, 1],
                                            [1, 0, 1],
                                            [1, 1, 1]]),
                                  np.array([[0], [0], [0], [1]]))
    or_networks = prepare_models(np.array([[0, 0, 1],
                                           [0, 1, 1],
                                           [1, 0, 1],
                                           [1, 1, 1]]),
                                 np.array([[0], [1], [1], [1]]))

    for i in range(40000):
        for x in xor_networks + and_networks + or_networks:
            x.feed_forward()
            x.back_prop()

    np.set_printoptions(precision=3, suppress=True)
    print("---  wyniki XOR   ---")
    print("Wynik prawidłowy:\n", xor_networks[0].y)
    for x in xor_networks:
        print("\nAktywator 1:", x.activator1, "Aktywator 2: ", x.activator2)
        print(x.output)
        print("Błąd: ",
              float(sum((x.output - xor_networks[0].y) ** 2)))

    print("\n\n---  wyniki AND   ---")
    print("Expected:\n", and_networks[0].y)
    for x in and_networks:
        print("\nAktywator 1:", x.activator1, "Aktywator 2: ", x.activator2)
        print(x.output)
        print("Błąd: ",
              float(sum((x.output - and_networks[0].y) ** 2)))

    print("\n\n---  wyniki OR    ---")
    print("Expected:\n", or_networks[0].y)
    for x in or_networks:
        print("\nAktywator 1:", x.activator1, "Aktywator 2: ", x.activator2)
        print(x.output)
        print("Błąd: ",
              float(sum((x.output - or_networks[0].y) ** 2)))

