#!/usr/bin/python3
"""This scriot sends a request ro
a url and displays the body"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    if res.status_code == 200:
        print(res.text)
