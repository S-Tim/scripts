#!/usr/bin/env bash

# Creates a basic git repository
# Author: Tim Silhan

mkdir -p .git/{refs,objects}
echo "ref: refs/heads/master" >> .git/HEAD
