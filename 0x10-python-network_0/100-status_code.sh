#!/usr/bin/env bash
# this script prints only status code
curl -sI -o /dev/null  -w "%{http_code}" $1
