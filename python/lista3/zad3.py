#!/usr/bin/python3

import os, sys

filename =  sys.argv[1]
with open(filename, 'r') as f:
    data = f.read()

bitesSum = sum([int(line.split()[-1]) for line in data.splitlines()])
print('Całkowita liczba bajtów: ', bitesSum)
