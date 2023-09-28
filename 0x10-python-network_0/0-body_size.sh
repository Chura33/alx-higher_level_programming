#!/bin/bash
# This script takes a URL as an argument, sends a request, and displays the response body size in bytes.

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

response_body=$(curl -s "$url")

body_size=$(echo -n "$response_body" | wc -c)
echo "$body_size"
