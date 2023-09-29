#!/usr/bin/python3
"""This script accesses my github and prints my id"""
import requests
import sys

if  __name__ == "__main__":
    url = "https://{}@github.com/{}".format(sys.argv[1], sys.argv[2])
    print(url)
    response = requests.get(url)
    try:
        if response:
            print(response.get('id'))
        else:
            print(None)
    except ValueError:
        print("Not a valid JSON")
