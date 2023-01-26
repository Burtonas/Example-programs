# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:28:13 2023

@author: owies
"""

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://py4e-data.dr-chuck.net/comments_42.json'
sum = 0

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    
    try:
        info = json.loads(data)
    except:
        info = None

    for entry in info['comments']:
        sum = sum + int(entry['count'])
    break
        
print('Sum:', sum)
