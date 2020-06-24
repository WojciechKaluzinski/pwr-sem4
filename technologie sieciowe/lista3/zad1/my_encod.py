import main_func1 as mf
import random as rand


def random_bits():
    out = ""
    for x in range(2137):
        out += "{0:b}".format(rand.randint(2 ^ 31, 2 ^ 32))
    return out


def rand_file(rand_filename):
    with open(rand_filename, 'w') as f:
        f.write(random_bits())


def enc_file(in_file, out_file):
    with open(in_file, 'r') as f:
        open(out_file, 'w').write(mf.enc_frame(f.read()))


def main():
    rand_file("dane_wejsciowe.txt")  # tworzę randomowy plik testowy wypełniony 0 i 1
    enc_file("dane_wejsciowe.txt", "zakodowane.txt")  # koduję plik wejściowy


if __name__ == '__main__':
    main()
