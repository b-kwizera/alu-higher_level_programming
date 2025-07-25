#!/usr/bin/python3
"""Sends a POST request to a URL with an email as parameter and displays the response"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    print(response.read().decode('utf-8'))
