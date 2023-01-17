#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)"""
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            response.read().decode('utf-8')
    except HTTPError as e:
        print('Error code: ', e.code)
