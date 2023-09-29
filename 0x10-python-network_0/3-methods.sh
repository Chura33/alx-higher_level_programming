#!/bin/bash
# This script prints all the methods that a server will accept
curl -sX OPTIONS -I $1 | grep -i 'allow' | awk -F ': ' '{print $2}'
