#!/usr/bin/python3
""" Takes your Github credentials (username and password)
    and uses the Github API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    response = requests.get(url)
    data = response.json()

    for commit in data[:10]:
        print(commit.get('sha'), end=": ")
        print(commit.get('commit').get('author').get('name'))
