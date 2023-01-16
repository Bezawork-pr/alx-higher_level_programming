#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
# Answer with pipe curl -sI GET "$1" | head -n 1 | cut -d$' ' -f2
# -s = Don't show download progress
# -o /dev/null = don't display the body
# -w "%{http_code}" = Write http response code to stdout after exit
# -w "%{http_code} prints the status code
curl -s -o /dev/null -I -w "%{http_code}" "$1"
