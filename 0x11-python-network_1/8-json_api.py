#!/usr/bin/python3
""" This script takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
    data = {'q': letter}
    response = requests.post(url, data=data)
    try:
        json_response = response.json()
        if json_response:
            print('[{}] {}'.format(json_response['id'], json_response['name']))
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
