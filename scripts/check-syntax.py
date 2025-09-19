#!/usr/bin/env python
#
# Tests the syntax the model file
#
import sys

from shared import load_models, ParseError, print_parse_error


try:
    load_models()
except ParseError as e:
    print_parse_error(e)
    sys.exit(1)

print('ok')
