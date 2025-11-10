import re

from socks import PRINTABLE_PROXY_TYPES

try:
    with open('sample_access.log', 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print('File is not found')
print(len(lines))


gets = 0
posts = 0
deletes = 0
puts = 0
urls = []
empty_urls = []
for line in lines:
    parts = line.strip()
    if not line:
        continue
    parts = line.split()
    method = parts[5].replace('"', '')
    if method == 'GET':
        gets += 1
    elif method == 'POST':
        posts += 1
    elif method == 'DELETE':
        deletes += 1
    elif method == 'PUT':
        puts += 1
    else:
        print(method)
    #link
    if len(parts) > 6 and parts[6].startswith('/'):
        url = parts[6]
        if len(url) > 1:
            urls.append(url)
        else:
            empty_urls.append(url)
    else:
        print("unknown")





