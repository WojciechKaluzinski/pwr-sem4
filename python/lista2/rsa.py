#! /usr/bin/python3
import math
import sys
import random


def pierwsza(rozmiar):
    liczba = 0
    while not test_millera_rabina(liczba, 20):
        liczba = random.randrange(10 ** rozmiar, 10 ** (rozmiar + 1) - 1, 1)
    return liczba



def modulo_potega(podstawa, potega, modulo):
    wynik = 1
    podstawa = podstawa % modulo
    while potega > 0:
        if potega % 2 == 1:
            wynik = (wynik * podstawa) % modulo
        potega = int(potega) >> 1
        podstawa = (podstawa * podstawa) % modulo
    return wynik



def odwr_mnozenie(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    pom_phi = phi

    while e > 0:
        pom1 = pom_phi // e
        pom2 = pom_phi - pom1 * e
        pom_phi = e
        e = pom2

        x = x2 - pom1 * x1
        y = d - pom1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if pom_phi == 1:
        return d + phi



def test_millera_rabina(n, rounds):
    if n != int(n):
        return False
    n = int(n)
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def element_pom(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(rounds):
        a = random.randrange(2, n)
        if element_pom(a):
            return False
    return True



def szufruj(n, e, tekst):
    szyfr = ""
    for char in tekst:
        szyfr += str(modulo_potega(ord(char), e, n)) + " "
    szyfr = szyfr[:-1]
    return szyfr


def deszufruj(n, d, tekst):
    slowa = tekst.split()
    wynik = ""
    for word in slowa:
        wynik += chr(modulo_potega(int(word), d, n))
    return wynik


try:
    instrukcja = sys.argv[1]

    if instrukcja == "--gen-keys":
        rozmiar = int(sys.argv[2])
        rozmiar = int(math.log(2) / math.log(10) * rozmiar)
        p = pierwsza(rozmiar)
        q = pierwsza(rozmiar)
        n = p * q
        fi = (p - 1) * (q - 1)
        e = 2
        while not math.gcd(e, fi) == 1:
            e = random.randrange(2, fi, 1)
        d = odwr_mnozenie(e, fi)

        with open("key.pub", "w") as f:
            f.write(str(n)+" "+str(e))
        with open("key.prv", "w") as f:
            f.write(str(n)+" "+str(d))

    elif instrukcja == "--encrypt":
        tekst = str(sys.argv[2])
        with open("key.pub", "r") as f:
            slowa = f.read().split()
            n = int(slowa[0])
            e = int(slowa[1])
        try:
            with open(tekst, "r") as f:
                tekst = szufruj(n, e, f.read())
        except FileNotFoundError:
            tekst = (szufruj(n, e, tekst))
        try:
            with open(sys.argv[3], "w") as f:
                f.write(tekst)
        except IndexError:
            print(tekst)

    elif instrukcja == "--decrypt":
        try:
            with open(sys.argv[2], "r") as f:
                tekst = f.read()
        except (FileNotFoundError, OSError):
            tekst = sys.argv[2]
        with open("key.prv", "r") as f:
            linie = f.read().split()
            n = int(linie[0])
            d = int(linie[1])
        try:
            with open(sys.argv[3], "w") as f:
                f.write(deszufruj(n, d, tekst))
        except IndexError:
            print(deszufruj(n, d, tekst))
    else:
        raise IndexError
except IndexError:
    print("Typ:", "--gen-keys [rozmiar]", "--encrypt [plik/string] [to file]", "--decrypt [plik/string]", sep="\n    ")

except FileNotFoundError:
    print("Plik nie istnieje")
except:
    print("Nieprawidłowe klucze")
