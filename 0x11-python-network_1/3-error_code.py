#!/usr/bin/python3
"""
 Sends a POST request to the passed URL with the email as
 a parameter, and displays the body of the response
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1], data) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
