#!/bin/bash
# This script sends a GET request to a URL using curl and displays the response body for a 200 status code.
if curl -I -s "http://$1" | grep -q "^HTTP/1.1 200 OK"; then curl -s "http://$1" | awk 'NR>1'; fi
