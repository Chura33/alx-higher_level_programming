#!/bin/bash
# This script sends a GET request to a URL, displays the body of the response for a 200 status code.

curl -s -o /tmp/body "$1" -I | grep "HTTP/1.1 200 OK" && cat /tmp/body
