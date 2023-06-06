#!/usr/bin/python3
for i in range(97, 123):
    if f"{i:c}" != "q" and f"{i:c}" != "e":
        print("{i:c}".format(i=i), end="")
