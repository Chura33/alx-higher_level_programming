#!/usr/bin/python3
""" This script takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1]
    if not letter:
        letter = ""
    data = {'q': letter}
    response = requests.post(url, data=data)
    json_response = response.json()
    if response.json():
        print('[{}] {}'.format(json_response.get('id'), json_response.get('name')))
    elif not response.json():
        print('No result')
    else:
        print("Not a valid JSON")
