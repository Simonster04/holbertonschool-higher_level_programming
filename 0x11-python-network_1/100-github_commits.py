#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest) of the
   repository. argv1 is the repo name, argv2 is owner name
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
