#!/usr/bin/env python3

import sys

substitution_map = {
    'a': 'n',
    'b': 'o',
    'c': 'p',
    'd': 'q',
    'e': 'r',
    'f': 's',
    'g': 't',
    'h': 'u',
    'i': 'v',
    'j': 'w',
    'k': 'x',
    'l': 'y',
    'm': 'z',
    'n': 'a',
    'o': 'b',
    'p': 'c',
    'q': 'd',
    'r': 'e',
    's': 'f',
    't': 'g',
    'u': 'h',
    'v': 'i',
    'w': 'j',
    'x': 'k',
    'y': 'l',
    'z': 'm',
}


def decrypt(input_text):
    inverse_substitution_map = {y: x for x, y in substitution_map.items()}
    return substitute(input_text, inverse_substitution_map)


def encrypt(input_text):
    return substitute(input_text, substitution_map)


def substitute(input_text, mapping):
    output_text = ''
    for char in input_text:
        if char in mapping.keys():
            output_text += mapping[char]
        else:
            output_text += char
    return output_text


def rot(input_text, rotation):
    characters = [char for char in 'abcdefghijklmnopqrstuvwxyz']
    mapping = {y: characters[(x+rotation) % len(characters)]
               for x, y in enumerate(characters)}

    return substitute(input_text, mapping)


if len(sys.argv) > 1:
    input_text = sys.argv[1].lower()

print(input_text)
print(rot(input_text, 13))
print(decrypt(rot(input_text, 13)))
