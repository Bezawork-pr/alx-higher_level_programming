#!/usr/bin/python3
"""a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    url + "?" + q
    response = requests.post(url)
    if reponse.json() != {}:
        print("[{}] {}".format(reponse.get("id"), response.get("name")))
    elif response.text == {}:
        print("No result")
    else:
        print("Not a valid JSON")

