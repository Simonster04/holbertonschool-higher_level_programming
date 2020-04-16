#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
from sys import argv

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    letter = ""
    try:
        letter = argv[1]
    except:
        pass
    var = {'q': letter}
    r = requests.post(url, data=var)
    if len(r.json()) > 0:
        print("[{}] {}".format(r.json()['id'], r.json()['name']))
    elif r.json() == {}:
        print("No result")
    else:
        print("Not a valid JSON")
