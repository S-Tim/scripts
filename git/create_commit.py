#!/usr/bin/env python3

import sys
import zlib
import time
from hashlib import sha1
from run_commands import run_command

# Hash of the tree from create_tree
ref_hash = '97b49d4c943e3715fe30f141cc6f27a8548cee0e'
if len(sys.argv) > 1:
    ref_hash = sys.argv[1]

print('Ref Hash: ', ref_hash)

# TODO Add parent if available
author_name = 'John Doe'
author_email = 'jd@someplace.com'
seconds_since_epoch = int(time.time())
time_zone = '+0000'
commit_message = 'This is it!\n'

content = f'\nauthor {author_name} <{author_email}> {seconds_since_epoch} {time_zone}'
content += f'\ncommitter {author_name} <{author_email}> {seconds_since_epoch} {time_zone}'
content += f'\n\n{commit_message}'
content = f'tree {ref_hash}' + content
# content = b'tree ' + bytes.fromhex(ref_hash) + content.encode('utf-8')
print('Content:', content)

header = f'commit {len(content)}\u0000'
print('Header:', header)

store = header.encode('utf-8') + content.encode('utf-8')
print('Store:', store)

digest = sha1(store).hexdigest()
print('Digest:', digest)

compressed = zlib.compress(store)
print('Compressed:', compressed)

print('Dir:', digest[:2])
print('File:', digest[2:])

run_command(f'mkdir -p .git/objects/{digest[:2]}')
with open(f'.git/objects/{digest[:2]}/{digest[2:]}', 'wb') as blob:
    blob.write(compressed)
