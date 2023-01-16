#!/bin/bash
# a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X POST "$1" -H "Content-Type: application/json" -d "$2"
