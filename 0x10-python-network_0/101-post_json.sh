#!/usr/bin/env bash
# This scripts curls a JSON file
curl -X POST -d "@$2" -H "Content-Type: application/json" $1
