#!/usr/bin/env python
#
# Show statistics about the model list
#
import sys

from shared import (
    load_models,
    ParseError,
    print_parse_error,
    format_codes,
)


try:
    models = load_models()
except ParseError as e:
    print_parse_error(e)
    sys.exit(1)


def p(m, desc):
    a = f'{m:3} ({m / n * 100:.1f}%) {desc}'
    b = ' ' * (40 - len(a))
    c = f'vs {n - m:3} ({(n - m) / n * 100:.1f}%)'
    print(f'{a}{b}{c}')


#
# Model count, code, author-provided code, PMR
#
n = len(models)
print('Syntax ok')
print('-' * 79)
print(f'{n} Models loaded')

n_code = 0
for m in models:
    n_code += 1 if m.has_code() else 0
p(n_code, 'have code')

n_author = 0
for m in models:
    n_author += 1 if m.has_author_provided_code() else 0
p(n_author, 'have author-provided code')

n_pmr = 0
for m in models:
    n_pmr += 1 if m.on_pmr() else 0
p(n_pmr, 'are on PMR')
print('-' * 79)

#
# Author-sanctioned formats
#
counts = {k: 0 for k in format_codes}
for m in models:
    for org in m.author_provided_formats():
        counts[org] += 1
print('Author-sanctioned formats:')
for k, v in sorted(counts.items(), key=lambda x: -x[1]):
    name = format_codes[k]
    print(name + ' ' * (14 - len(name)) + f'{v:3d}')
print()


#
# Author-sanctioned formats, since year X
#
def since(year):
    counts = {k: 0 for k in format_codes}
    for m in models:
        if m.year < year:
            continue
        for org in m.author_provided_formats():
            counts[org] += 1
    print(f'Author-sanctioned formats, since {year}:')
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        if v == 0:
            continue
        name = format_codes[k]
        print(name + ' ' * (14 - len(name)) + f'{v:3d}')
    print()


since(2011)
since(2020)

