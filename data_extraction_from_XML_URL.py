# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:28:51 2023

@author: owies
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl 

serviceurl = 'http://py4e-data.dr-chuck.net/comments_1691344.xml'
sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    
    url = serviceurl
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    decoded_data = data.decode()
    # print(decoded_data)
    
    tree = ET.fromstring(data)
    lst = tree.findall('.//comment')
    print('Count', len(lst))
    # names = tree.findall('.//name')
    # counts = tree.findall('.//count')
    # print('Name:', len(names))

    for item in lst:
        sum = sum + int(item.find('count').text)
    print('Sum:',sum)
