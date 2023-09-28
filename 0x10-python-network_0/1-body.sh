#!/bin/bash
# This script sends a GET request to a URL using curl and displays the response body for a 200 status code.
curl -si 0.0.0.0:5000|grep -iq "^HTTP/1.1 200 OK" && curl -L $1
