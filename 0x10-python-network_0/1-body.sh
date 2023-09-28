#!/bin/bash
# This script sends a GET request to a URL using curl and displays the response body for a 200 status code.
curl -si "$1" | awk 'NR==1{if($2==200)body=1}body'
