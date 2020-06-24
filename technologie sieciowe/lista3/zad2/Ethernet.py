from functools import reduce


class Collision(Exception):
    pass


def show_elem(e):
    return '__' if e is None else e[0]


def mkEthernet(length):
    return list(map(lambda _: None, range(length)))  # tworzę listę Ethernet


class Ethernet:
    def __init__(self, length):
        self.length = length
        self.ethernet = mkEthernet(length)

    def __str__(self):
        return reduce(
            lambda p, n: p + show_elem(n),
            self.ethernet,
            ' '
        )

    def clear(self):
        self.ethernet = mkEthernet(self.length)

    def emptyL(self):
        return self.ethernet[0] is None

    def emptyR(self):
        return self.ethernet[-1] is None

    def pushL(self, message):
        self.ethernet[0] = message, 1

    def pushR(self, message):
        self.ethernet[-1] = message, -1

    def action(self):  # symulacja przesyłu wiadomości
        newEthernet = mkEthernet(self.length)

        leftRecv = False
        rightRecv = False

        for i, e in enumerate(self.ethernet):
            if e is not None:
                message, direction = e
                position = i + direction
                if 0 <= position <= self.length - 1:  # jeśli nie doszedłeś do końca ethernetu to:
                    if newEthernet[position] is None:  # zgłoś kolizję gdy następna komórka nie jest pusta
                        if self.ethernet[position] is None:  # gdy następna komórka jest wolna zapełnij ją wiadomością
                            newEthernet[position] = message, direction
                        else:
                            message1, direction1 = self.ethernet[position]
                            if direction == direction1:  # zgłoś kolizję gdy napotkałeś na nie swoją wiadomość
                                newEthernet[position] = message, direction
                            else:
                                raise Collision()
                    else:
                        raise Collision()
                elif position < 0:  # gdy wiadomość doszła do lewego
                    leftRecv = True
                elif position >= self.length:  # gdy wiadomość doszła do prawego
                    rightRecv = True
        self.ethernet = newEthernet
        return leftRecv, rightRecv
    # end action
