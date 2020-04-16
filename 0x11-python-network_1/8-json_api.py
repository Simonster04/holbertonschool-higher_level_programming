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
    try:
        data = r.json()
        if len(data) > 0:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
