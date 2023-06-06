#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        res = ord(str[i])
        if res >= 97:
            res -= 32
        print("{res:c}".format(res=res), end=" ")
