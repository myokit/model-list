#!/usr/bin/env python
#
# Creates plots based on the model list and manually gathered PMR data.
#
import sys

from shared import load_models, ParseError, print_parse_error

if __name__ == '__main__':
    try:
        models = load_models()
    except ParseError as e:
        print_parse_error(e)
        sys.exit(1)

    n = len(models)
    print('Syntax ok')
    print('-' * 79)
    print(f'{n} Models loaded')

    def p(m, desc):
        a = f'{m:3} ({m / n * 100:.1f}%) {desc}'
        b = ' ' * (40 - len(a))
        c = f'vs {n - m:3} ({(n - m) / n * 100:.1f}%)'
        print(f'{a}{b}{c}')


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


    sys.exit(0)

