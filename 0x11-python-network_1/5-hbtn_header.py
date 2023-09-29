#!/usr/bin/python3
"""
Write a Python script that
takes in a URL, sends a request
to the URL and displays
the value of the variable
X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code == 200:
        if 'X-Request-Id' in response.headers:
            request_id = response.headers.get("X-Request-Id")
            print("X-Request-Id:", request_id)
        else:
            print("id not found")
    else:
        print("error occurred")
