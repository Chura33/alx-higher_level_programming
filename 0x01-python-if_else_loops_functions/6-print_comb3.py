#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1 + i, 10):
        if i == 8:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
