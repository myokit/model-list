#!/usr/bin/env python
#
# Shows models that are on PMR, and lists their PMR workspaces (converting
# exposures to workspaces via PMR's API).
#
import json
import sys
import urllib.request

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


if __name__ == '__main__':
    try:
        models = load_models()
    except ParseError as e:
        print_parse_error(e)
        sys.exit(1)

    for model in models:
        pmr = model.pmr_link()
        if pmr is not None:
            print(model, history_link(pmr))

