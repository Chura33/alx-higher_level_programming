#!/bin/bash
# This script sends a GET request to a URL using curl and displays the response body for a 200 status code.
curl -si "$1" | { IFS= read -r line; [ "$line" = "HTTP/1.1 200 OK" ] && cat || echo "$line"; }
