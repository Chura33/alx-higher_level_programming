#!/bin/bash
# this script sends a post request to the ipaddress
curl -sX POST -d "email:test@gmail.com&subject:I will always be here for PLD" $1
