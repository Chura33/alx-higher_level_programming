#!/usr/bin/python3
"""This script fetches a given url"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content:{}".format((resp.text)))
