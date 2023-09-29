#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status """
import urllib.request
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')
    print("Body response:")
    print("    - type: {}".format(type(body)))
    print("    - content: {}".format(body))
    print("    - utf8 content: {}".format(utf8_content))
