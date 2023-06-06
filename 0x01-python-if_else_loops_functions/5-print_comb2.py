#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{i}".format(i=i))
    else:
        print("{i:02}".format(i=i), end=", ")
