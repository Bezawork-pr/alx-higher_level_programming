#!/usr/bin/python3
"""a Python script that takes GitHub credentials
username and password) and uses the GitHub API to display your id"""
from requests.auth import HTTPBasicAuth
import requests
import sys

if __name__ == "__main__":
    basicauth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get(' https://api.github.com/user', auth=basicauth)
    print("{}".format(req.json().get("id")))
