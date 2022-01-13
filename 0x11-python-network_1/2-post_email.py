#!/usr/bin/python3
"""
Takes in a URL and and eamil, sends a post reqeust to the passed URL
with the email as a parameter, and displays the body of the
response(decorded in utf-8)
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    param = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(param).encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
