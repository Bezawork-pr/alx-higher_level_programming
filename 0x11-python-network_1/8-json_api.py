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
    response = requests.post(url, data={'q': q})
    try:
        response = response.json()
        if reponse == {}:
            print("No result")
        else:
            print("[{}] {}".format(reponse.get("id"), response.get("name")))
    except Exception as error:
        print("Not a valid JSON")