#!/usr/bin/env bash

# Generates commits that each add a ranodm text file to the repository. The
# content of the file is the filename itself without the extension. The number
# of commits to be generated has to be passed as an argument.
#
# Author: Tim Silhan

function generateCommit {
    chars=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    string=
    for i in {1..8} ; do
        string+="${chars:RANDOM%${#chars}:1}"
    done
    echo $string >> $string.txt
    git add --all
    git commit -m "Added $string.txt"
}

echo "Generating $1 commits"
for j in $(seq 1 $1) ; do
    generateCommit
done

