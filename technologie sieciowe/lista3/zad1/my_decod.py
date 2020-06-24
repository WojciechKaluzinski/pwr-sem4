import main_func1 as mf


def dec_file(in_file, out_file):
    with open(in_file, 'r') as input_file:
        open(out_file, 'w').write(mf.dec_frame(input_file.read()))


def main():
    dec_file("zakodowane.txt", "zdekodowane.txt")  # dekoduję zakodowny plik


if __name__ == "__main__":
    main()
