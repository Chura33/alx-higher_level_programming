#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Prepare the data to send in the POST request
data = {'email': email}
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data)

try:
    with urllib.request.urlopen(req) as response:
        res = response.read().decode('utf-8')
    print(res)
except urllib.error.URLError as e:
    print("URLError:", e)
except urllib.error.HTTPError as e:
    print("HTTPError:", e)
except Exception as e:
    print("An error occurred:", e)
