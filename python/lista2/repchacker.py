#!/usr/bin/python3

import sys
import os
import hashlib
from collections import defaultdict

folder = sys.argv[1]
#folder = "/home/wojtek/Pulpit/sem4/python"    #"../../" 


def md5_generator(fname, part_size=1024):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        part = f.read(part_size)
        while part:
            hash.update(part)
            part = f.read(part_size)
    return hash.hexdigest()


if __name__ == "__main__":

    md5_dict = defaultdict(list)

    file_types = ["ppt", "pptx", "pdf", "txt", "html",
                          "mp4", "jpg", "png", "xls", "xlsx", "xml",
                          "vsd", "py", "json"]

    # Przeglądam wszystkie pliki i podfoldery
    for path, dirs, files in os.walk(folder):
        for each_file in files:
            if each_file.split(".")[-1].lower() in file_types:
                # Aktualizuje ścieżkę dla każdego podfolderu
                file_path = os.path.join(os.path.abspath(path), each_file)
                # Dodaję kody do listy
                md5_dict[md5_generator(file_path)].append(file_path)

    # Biorę pod uwagę jedynie klucze mające więcej niz jedną wartość
    duplicate = list((
        val for key, val in md5_dict.items() if len(val) > 1))
    # Wyświetlanie duplikatów
    for i in range (len(duplicate)):
        for j in range (len(duplicate[i])):
            print(duplicate[i][j])
        print("------------------------")
