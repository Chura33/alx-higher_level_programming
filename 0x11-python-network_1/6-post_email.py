#!/usr/bin/python3
"""This script posts to the passed address"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL and email from the command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email parameter
    data = {'email': email}

    try:
        # Send a POST request with the data
        response = requests.post(url, data=data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print(response.text)
        else:
            print('Request failed with status code:', response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
