#!/usr/bin/python3
"""
takes in a URL, sends a request
to the URL and displays
the body of the response
"""
import urllib.request
import urllib.error
import sys

# Get the URL from the command-line argument
url = sys.argv[1]
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(url) as response:
            # Check if the response is an HTTP error
            if response.getcode() != 200:
                print("Error code:", response.getcode())
            else:
                res = response.read().decode('utf-8')
                print(res)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
    except Exception as e:
        print("An error occurred:", e)
