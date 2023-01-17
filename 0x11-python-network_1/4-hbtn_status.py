#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    content = requests.get(url, auth=('user', 'pass'))
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.encoding))
