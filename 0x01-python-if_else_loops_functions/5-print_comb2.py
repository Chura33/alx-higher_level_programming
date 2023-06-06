#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{i}\n".format(i=i))
    else:
        print("{i}".format(i=i), end=", ")
