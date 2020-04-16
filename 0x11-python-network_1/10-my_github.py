#!/usr/bin/python3
""" Takes your Github credentials (username and password)
    and uses the Github API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":

    user = argv[1]
    pswd = argv[2]
    response = requests.get('https://api.github.com/user', auth=(user, pswd))
    print(response.json().get('id'))
