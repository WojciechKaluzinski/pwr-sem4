#!/usr/bin/python3

m=["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]
print([[m[j].split()[i] for j in range(len(m))] for i in range(len(m[0].split()))])


