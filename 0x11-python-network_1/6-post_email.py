#!/usr/bin/python3
"""This script posts to the passed address"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    try:
        response = requests.post(url, data=data)

        if response.status_code == 200:
            print(response.text)
        else:
            print('Request failed with status code:', response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
