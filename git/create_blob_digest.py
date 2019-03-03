#!/usr/bin/env python3

import sys
from hashlib import sha1

content = 'Hello World'
if len(sys.argv) > 1:
    content = sys.argv[1]

print('Input: ', content)

header = f'blob {len(content)}\u0000'
print('Header: ', header)

store = header + content
print('Store: ', store)

digest = sha1(store.encode('utf-8')).hexdigest()
print('Digest: ', digest)
