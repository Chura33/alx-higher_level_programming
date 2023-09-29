#!/usr/bin/python3
"""This script accesses my github and prints my id"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    authent = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = "https://api.github.com/user"
    response = requests.get(url, auth=authent)
    try:
        if response:
            print(response.json().get('id'))
        else:
            print(None)
    except ValueError as e:
        print(e)
