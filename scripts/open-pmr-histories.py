#!/usr/bin/env python
#
# Scans for models that are on PMR, constructs a link to their history pages,
# and opens them in a browser.
#
import json
import sys
import urllib.request
import webbrowser

from shared import load_models, ParseError, print_parse_error


def history_link(pmr):
    """
    Turns a workspace or exposure link into a link to the history page.
    """
    # Get workspace link from exposures
    a = 'https://models.physiomeproject.org/workspace/'
    b = 'https://models.physiomeproject.org/w/'
    if not (pmr.startswith(a) or pmr.startswith(b)):
        try:
            hds = {'Accept': 'application/vnd.physiome.pmr2.json.1'}
            req = urllib.request.Request(pmr, headers=hds)

            with urllib.request.urlopen(req) as r:
                r = r.read()[:10000]    # Limit size, for security
            r = json.loads(r)

            url = None
            for link in r['collection']['links']:
                if link['prompt'] == 'Workspace URL':
                    url = link['href']
                    break
            if url is None:
                raise Exception('No link with prompt=Workspace URL found')
            pmr = url

        except Exception as e:
            raise Exception(f'Unable to locate workspace for {pmr}') from e

    # Append the history bit
    page = '@@shortlog'
    if pmr.endswith('/'):
        return f'{pmr}{page}'
    return f'{pmr}/{page}'


try:
    models = load_models()
except ParseError as e:
    print_parse_error(e)
    sys.exit(1)

print('This script is about to make several HTTP requests to convert')
print(' links to PMR exposures into workspace links, and will then open')
print(' several browser windows.')
ok = input('Continue (y/n)? ').strip().lower()
if ok not in ('y', 'yes'):
    print('Halted')
    sys.exit(1)

print('"Tag","Year added","Author"')
for model in models:
    pmr = model.pmr_link()
    if pmr is not None:
        pmr = history_link(pmr)
        webbrowser.open(pmr)
        print(f'"{model.key}",20,""')

