#!/bin/bash
# This script sends a GET request to a URL using curl and displays the response body for a 200 status code.
curl -sI "$1" | grep "HTTP/1.1 200 OK" && curl -si "$1"
