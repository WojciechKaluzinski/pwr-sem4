#! /usr/bin/python3
import os
import sys


def change(directory):
    directory = os.path.join(os.getcwd(),directory)
    directory_list = os.listdir(directory)

    for x in directory_list:
        tmp = os.path.join(directory, x)
        if os.path.isdir(tmp):
            change(os.path.join(directory, x))
	 rename(tmp,os.path.join(directory, x.lower())) 
        # print(tmp,os.path.join(directory, x.lower()))

try:
    change(sys.argv[1])

except (IndexError, FileNotFoundError):
    print("Zły argument")
