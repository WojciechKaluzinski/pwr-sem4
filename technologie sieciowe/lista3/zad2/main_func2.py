

from Ethernet import Ethernet, Collision
from random import random, randint
from time import sleep

PACKET_SIZE = 0
P = 0.1
ETHERNET_SIZE = 0
FAILS_COUNT = 0
SUCCESSES_COUNT = 0


class Router:
    def __init__(self, empty, push, message, P):  # parametry routera
        self.empty = empty
        self.push = push
        self.message = message
        self.P = P

        self.wait = 0
        self.sent = 0
        self.rem = 0
        self.crash = 0

    def action(self):  # emitowanie wiadomości przez router
        if self.rem > 0:
            self.push(self.message)
            self.rem -= 1
            self.sent += 1
        elif self.sent > 0:
            return
        elif self.wait == 0:
            if self.empty and random() < P:
                self.push(self.message)
                self.rem = PACKET_SIZE - 1
                self.sent = 1
        else:
            self.wait -= 1

    def collision(self):  # obsługa kolizji
        self.rem = 0
        self.crash += 1
        self.sent = 0
        if self.crash < 10:  # algorytm zwiększania czasu oczekiwania po kolizjach
            self.wait = randint(1, 2 ** self.crash)
        else:
            print('Nie można wysłaś wiadomości: ' + self.message)
            self.crash = 0
            self.wait = 0

    def delivered(self):  # obsługa dostarczonych wiadomości
        global SUCCESSES_COUNT
        self.sent -= 1
        if self.sent == 0:
            self.crash = 0
            SUCCESSES_COUNT += 1
            print('Dostarczono wiadomość: ' + self.message)


if __name__ == "__main__":

    print("wprowadź rozmiar wysyłanego pakietu: ")
    PACKET_SIZE = int(input())
    print("wprowadź rozmiar Ethernetu: ")
    ETHERNET_SIZE = int(input())
    ethernet = Ethernet(ETHERNET_SIZE)  # tworzę obikekt ethernet o zadanej wielkości

    left_router = Router(ethernet.emptyL, ethernet.pushL, '->', P)  # tworzę lewe urządzenie - czyszczę kabel
    right_router = Router(ethernet.emptyR, ethernet.pushR, '<-', P)  # tworzę prawe urządzenie - czyszczę kabel

    while True:
        try:
            left_router.action()  # nadawaje lewym
            right_router.action()  # nadawaje prawym

            print(ethernet)
            L, R = ethernet.action()  # akcja w kablu

            if L:
                right_router.delivered()  # dostarczono prawy
            if R:
                left_router.delivered()  # dostarczono lewy
            sleep(0.03)
        except Collision:  # gdy sygnały nie zostały dostarczone uruchom kolizję
            print('Nastąpiła kolizja')
            FAILS_COUNT += 1
            ethernet.clear()
            left_router.collision()
            right_router.collision()
        except KeyboardInterrupt:  # zatrzymywanie testów
            print("rozmiar wysyłanego pakietu: ", PACKET_SIZE)
            print("rozmiar Ethernetu: ", ETHERNET_SIZE)
            print("wykonano: ", SUCCESSES_COUNT + FAILS_COUNT, " prób")
            print("dostarczono: ", SUCCESSES_COUNT, " wiadomości")
            print("zanotowano: ", FAILS_COUNT, " kolizji")
            print("sprawność: ", int((SUCCESSES_COUNT / (SUCCESSES_COUNT + FAILS_COUNT)) * 100), "%")
            break
