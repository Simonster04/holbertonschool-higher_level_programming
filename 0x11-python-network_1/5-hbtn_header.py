#!/usr/bin/python3
"""
 Sends a request to the URL and displays the value of
 the X-Request-Id variable found in the header of the response
"""

import requests
from sys import argv


if __name__ == "__main__":
    try:
        r = requests.get(argv[1])
        print(r.headers['X-Request-Id'])
    except:
        pass