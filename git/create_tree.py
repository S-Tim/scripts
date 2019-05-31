#!/usr/bin/env python3

# Creates a git tree object from the given hash and filename
# The format of a tree object is:
#   tree [content size]\u0000[Entries having references to other trees and blobs]
# With each entry having the format:
#   [mode] [file/directory name]\u0000[SHA-1 of referenced blob or tree (as bytes)]
# Reference: https://stackoverflow.com/questions/14790681/what-is-the-internal-format-of-a-git-tree-object
#
# Author: Tim Silhan

import sys
import zlib
from hashlib import sha1
from run_commands import run_command

ref_hash = '557db03de997c86a4a028e1ebd3a1ceb225be238'
if len(sys.argv) > 1:
    ref_hash = sys.argv[1]

filename = "hello.txt"
if len(sys.argv) > 2:
    filename = sys.argv[2]

print('Ref Hash: ', ref_hash)

content = b"100644 " + filename.encode('utf-8') + b"\x00" + bytes.fromhex(ref_hash)
# Create a directory with a tree object
# content = b"40000 " + filename.encode('utf-8') + b"\x00" + bytes.fromhex(ref_hash)

header = f'tree {len(content)}\u0000'
print('Header:', header)

store = header.encode('utf-8') + content
print('Store:', store)

digest = sha1(store).hexdigest()
print('Digest:', digest)
print('Dir:', digest[:2])
print('File:', digest[2:])

compressed = zlib.compress(store)
print('Compressed:', compressed)

run_command(f'mkdir -p .git/objects/{digest[:2]}')
with open(f'.git/objects/{digest[:2]}/{digest[2:]}', 'wb') as blob:
    blob.write(compressed)
