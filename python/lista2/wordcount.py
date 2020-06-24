#!/usr/bin/python3

import os, sys

filename = sys.argv[1]
size = os.stat(filename).st_size
print('File size ::', size)

with open(filename, 'r') as f:
    data = f.read()
    line = data.splitlines()
    max_val = max(line, key=len)
    words = data.split()
    spaces = data.split(" ")
    charc = (len(data) - len(spaces))

    print('Line number ::', len(line), '\nWords number ::', len(words), '\nMax line lenght ::', len(max_val))


