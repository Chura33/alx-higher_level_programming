#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        res = ord(str[i])
        if res >= 97:
            res -= 32
        if i == len(str) - 1:
            print("{res:c}".format(res=res))
        else:
            print("{res:c}".format(res=res), end="")
