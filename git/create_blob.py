#!/usr/bin/env python3

import sys
import zlib
from hashlib import sha1
from run_commands import run_command

content = 'Hello World\n'
if len(sys.argv) > 1:
    content = sys.argv[1]

print('Input: ', content)

header = f'blob {len(content)}\u0000'
print('Header:', header)

store = header + content
print('Store:', store)

digest = sha1(store.encode('utf-8')).hexdigest()
print('Digest:', digest)

compressed = zlib.compress(store.encode('utf-8'))
print('Compressed:', compressed)

print('Dir:', digest[:2])
print('File:', digest[2:])

run_command(f'mkdir -p .git/objects/{digest[:2]}')
with open(f'.git/objects/{digest[:2]}/{digest[2:]}', 'wb') as blob:
    blob.write(compressed)
