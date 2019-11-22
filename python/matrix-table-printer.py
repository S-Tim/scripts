#!/usr/bin/env python3

import sys
import itertools

# items = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
items = ['one', 'two', 'three', 'twenty']

def print_items(items):
    product = list(itertools.product(items, items))

    row_count = len(items)
    rows = [product[i * row_count : (i+1) * row_count] for i in range(row_count)]

    longest_entry = max(*[len(str(combined)) for combined in product])
    longest_item = max(*[len(str(item)) for item in items])
    separator = '    '

    # indent to fit the row labels on the left side
    print(' ' * longest_item + '|' + separator, end='')

    # column labels
    column_labels = [str(item).ljust(longest_entry + len(separator)) for item in items]
    print(*column_labels, sep='')

    # column underline
    print('_' * (longest_entry * row_count + row_count * len(separator) + longest_item + 1))

    # rows
    for index, row in enumerate(rows):
        row_with_padding = [str(entry).ljust(longest_entry) for entry in row]
        print(items[index].ljust(longest_item) + '|',  *row_with_padding, sep=separator)

print_items(items)
