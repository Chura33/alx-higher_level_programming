#!/bin/bash
# This script sends a GET request to a URL using curl and displays the response body for a 200 status code.
curl -s -w "%{http_code}" "$url" | awk 'NR==1 && $1==200 {p=1} p'
