#!/usr/bin/python3
"""
    This module prints the X-Request-Id
    variable in the response
"""

import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: ./1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.headers.get('X-Request-Id')
        if header is not None:
            print(header)
except Exception as e:
    print(e)
