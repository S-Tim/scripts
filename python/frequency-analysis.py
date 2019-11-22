#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("Provide a text as parameter")
    sys.exit()

input_text  = ''
with open(sys.argv[1], 'r') as input_file:
    input_text = input_file.read()

frequencies = {}

german = {
    'a' : 6.51,
    'b' : 1.89,
    'c' : 3.06,
    'd' : 5.08,
    'e' : 17.40,
    'f' : 1.66,
    'g' : 3.01,
    'h' : 4.76,
    'i' : 7.55,
    'j' : 0.27,
    'k' : 1.21,
    'l' : 3.44,
    'm' : 2.53,
    'n' : 9.78,
    'o' : 2.51,
    'p' : 0.79,
    'q' : 0.02,
    'r' : 7.00,
    's' : 7.27,
    't' : 6.15,
    'u' : 4.35,
    'v' : 0.67,
    'w' : 1.89,
    'x' : 0.03,
    'y' : 0.04,
    'z' : 1.13,
    'ß' : 0.31}

english = {
    'a' : 8.167,
    'b' : 1.492,
    'c' : 2.782,
    'd' : 4.253,
    'e' :  12.702,
    'f' : 2.228,
    'g' : 2.015,
    'h' : 6.094,
    'i' : 6.966,
    'j' : 0.153,
    'k' : 0.772,
    'l' : 4.025,
    'm' : 2.406,
    'n' : 6.749,
    'o' : 7.507,
    'p' : 1.929,
    'q' : 0.095,
    'r' : 5.987,
    's' : 6.327,
    't' : 9.056,
    'u' : 2.758,
    'v' : 0.978,
    'w' : 2.360,
    'x' : 0.150,
    'y' : 1.974,
    'z' : 0.074,
    'ß' : 0.00}

def calc_distance(text_frequency, language_frequency):
    distance = 0.0

    for char, frequency in text_frequency.items():
        if char in language_frequency.keys():
            distance += abs(frequency - language_frequency[char])
    
    return distance

excluded_characters = [' ', '.', ':', ',', '-', '(', ')', '\n']
case_sensitive = False

# prepare input
if not case_sensitive:
    input_text = input_text.lower()

for excluded_character in excluded_characters:
    input_text = input_text.replace(excluded_character, '')

# analyze frequency
for character in input_text:
    if character not in frequencies.keys():
        frequencies[character] = 0
    frequencies[character] += 1

for key, value in sorted(frequencies.items()):
    print(f'{key}: {value}, {round((value/len(input_text) * 100), 3)}')

distance_to_german = calc_distance({char: (prob/len(input_text)*100) for char, prob in frequencies.items() }, german)
distance_to_english = calc_distance({char: (prob/len(input_text)*100) for char, prob in frequencies.items() }, english)

print("Distance to German: ", distance_to_german)
print("Distance to English: ", distance_to_english)

if distance_to_german < distance_to_english:
    print("Text is probably German")
else:
    print("Text is probably English")
