#!/usr/bin/env python3

# Creates a git commit referencing the given tree object and descending from the given parent
# The format of a commit is:
# commit [content size]\u0000[content]
# With the content being:
#   tree [SHA-1 of the tree object]
#   [parents]
#   author {author_name} <{author_email}> {author_date_seconds} {author_date_timezone}
#   committer {committer_name} <{committer_email}> {committer_date_seconds} {committer_date_timezone}
#
#   [commit message]
# With the parent format:
#   parent [SHA-1 of parent-commit-1]
#   parent [SHA-1 of parent-commit-2]
#   ...
# And the date seconds being seconds since 1970, e.g. 946684800 is the first second of year 2000
# The timezone has the format +xxxx e.g.: +0000 is UTC
# Reference: https://stackoverflow.com/questions/22968856/what-is-the-file-format-of-a-git-commit-object
#
# Author: Tim Silhan

import sys
import zlib
import time
from hashlib import sha1
from run_commands import run_command

# Hash of the tree from create_tree
ref_hash = '97b49d4c943e3715fe30f141cc6f27a8548cee0e'
if len(sys.argv) > 1:
    ref_hash = sys.argv[1]

print('Tree Hash: ', ref_hash)

parent_hash = ''
if len(sys.argv) > 2:
    parent_hash = sys.argv[2]

if parent_hash:
    print('Parent Hash: ', parent_hash)

author_name = 'John Doe'
author_email = 'jd@someplace.com'
seconds_since_epoch = int(time.time())
time_zone = '+0000'
commit_message = 'This is it! We made it!\n'

content = ''
if parent_hash:
    content += f'\nparent {parent_hash}'
content += f'\nauthor {author_name} <{author_email}> {seconds_since_epoch} {time_zone}'
content += f'\ncommitter {author_name} <{author_email}> {seconds_since_epoch} {time_zone}'
content += f'\n\n{commit_message}'
content = f'tree {ref_hash}' + content
# content = b'tree ' + bytes.fromhex(ref_hash) + content.encode('utf-8')
print('Content:\n', content)

header = f'commit {len(content)}\u0000'
print('Header:', header)

store = header.encode('utf-8') + content.encode('utf-8')
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
