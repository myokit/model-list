#!/usr/bin/env python
#
# Syntax check and analysis on model list
#

# Location of model list
PATH = 'README.md'

# First entry
FIRST = '1962 Noble mPf'


# Regexes for parsing
_rhead = r'([0-9]{4}[a-z]?) ([A-Za-z\' -]+?) ([A-Za-z]+)'
_rbase = r'(\[[A-Za-z\' -]+) ([0-9]{4}[a-z]?)\]' \
         r'\(([#]?)([0-9]{4}[a-z]?-[A-Za-z-]+)\)'
_rlink = r'\[([^]]+)\]\(([^)]+?)\)'


# Structured entries
_struct = {
    'In Myokit repo': 'myokit_repo',

    'Paper': 'doi',
    'Chapter': 'doi',
    'Abstract': 'doi',
    'Preprint': 'doi',
    'Correction': 'doi_corr',
    'Physiome reproduction paper': 'doi_physiome',

    # Code used to generate results in the original publication
    'Original CellML': 'org_cellml',
    'Original C code': 'org_c',
    'Original C++ code': 'org_cpp',
    'Original Fortran code': 'org_fortran',
    'Original Matlab code': 'org_matlab',
    'Original Delphi code': 'org_delphi',
    'Original Visual Basic code': 'org_visbas',
    'Original simBio code': 'org_simbio',
    'Original openCARP code': 'org_carp',

    # Author-sanctioned code, e.g. CellML generated when writing the paper
    'Official CellML': 'off_cellml',
    'Official simBio code': 'off_simbio',
    'Official C code': 'off_c',

    # Updated code published by authors or others
    'Updated C++ code': 'upd_cpp',
    'Updated Matlab code': 'upd_matlab',
    'Updated Visual Basic code': 'upd_visbas',

    # New implementation, e.g. by a CellML curator
    'CellML reimplementation': 're_cellml',
    'Matlab reimplementation': 're_matlab',
}


class Model:
    """
    Model, as read from the list.
    """
    first = None
    year = None
    year_letter = None
    preparation = None

    bases = None

    doi = None
    doi_corr = None
    doi_physiome = None

    myokit_repo = None

    off_cellml = None
    off_simbio = None
    off_c = None

    org_cellml = None
    org_c = None
    org_cpp = None
    org_fortran = None
    org_matlab = None
    org_delphi = None
    org_visbas = None
    org_simbio = None
    org_carp = None

    upd_matlab = None
    upd_cpp = None
    upd_visbas = None

    # Lists of reimplementations
    re_cellml = None
    re_matlab = None

    def __init__(self, first, year, preparation, year_letter=None):
        self.first, self.year, self.preparation = first, year, preparation
        self.year_letter = year_letter

        y = year if year_letter is None else f'{year}{year_letter}'
        f = first.lower().replace(' ', '-').replace("'", '')
        p = self.preparation.lower()
        self.key = f'{y}-{f}-{p}'

        self.bases = []
        self.re_cellml = []
        self.re_matlab = []

    def __str__(self):
        return f'{self.year} {self.first} {self.preparation}'

    def __repr__(self):
        return f'Model<{self.first} {self.year} {self.preparation}>'

    def has_code(self):
        """
        Returns True if _any_ code is available for this model.
        """
        if self.myokit_repo:
            return True
        for k, v in vars(self).items():
            if v is not None and k.startswith(('off_', 'org_', 'upd_')):
                return True
            if k.startswith('re_') and len(v) > 0:
                return True
        return False

    def has_author_provided_code(self):
        """
        Returns True if author-provided code (official or original) is
        available, in any format.
        """
        return len(self.author_provided_formats()) > 0

    def on_pmr(self):
        """
        Returns True if this model is available from PMR.
        """
        return self.pmr_link() is not None

    def author_provided_formats(self):
        """
        Returns a list of formats in which original or official code is listed
        for this model.
        """
        orgs = set()
        for k, v in vars(self).items():
            if v is not None and k.startswith(('off_', 'org_')):
                orgs.add(k)
        return orgs

    def pmr_link(self):
        """
        Returns a PMR link, looking first at the ``org_cellml`` property, then
        ``off_cellml``, and finally ``pmr``.

        Returns ``None`` if no PMR link found.
        """
        for link in self.re_cellml + [self.org_cellml, self.off_cellml]:
            if link is not None:
                if link.startswith('https://models.physiomeproject.org/'):
                    return link
        return None


def _lvsd(s, t):
    """Returns the Levenshtein distance between two strings ``s`` and ``t``."""
    # This implementation is adapted from wikipedia:
    # en.wikipedia.org/wiki/Levenshtein_distance#Iterative_with_full_matrix
    if s == t:
        return 0
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)

    n = len(t) + 1
    v0 = list(range(n))
    v1 = [None] * n
    for i, si in enumerate(s):
        v1[0] = i + 1
        for j, tj in enumerate(t):
            v1[j + 1] = min(
                v0[j + 1] + 1, v1[j] + 1, v0[j] if si == tj else v0[j] + 1)
        v0, v1 = v1, v0
    return v0[n - 1]


def _didyoumean(key, options):
    """ Returns the closest ``(option, distance)`` pair to key. """
    return min(((k, _lvsd(key, k)) for k in options), key=lambda x: x[1])


class ParseError(RuntimeError):
    """
    Raised by ``load_models`` if something goes wrong.
    """

    def __init__(self, msg, entry=None):
        self.msg = msg
        self.entry = entry
        super().__init__(msg)


def print_parse_error(e, stream=None):
    """ Print an error. """
    if stream is None:
        from sys import stderr as stream
    if e.entry is not None:
        print('Error in:\n', file=stream)
        print(f'  ## {e.entry[0]}', file=stream)
        for line in e.entry[1:]:
            if len(line) > 77:
                print(f'  {line[:74]}...', file=stream)
            else:
                print(f'  {line}', file=stream)
        print(file=stream)
    print(e.msg, file=stream)


# Year parser
def _parse_year(text, entry):
    """ Parses a year, with an optional letter at the end. """
    letter = None
    if len(text) > 4:
        letter = text[4:]
        if len(letter) > 1 or letter not in 'abcdefg':
            raise ParseError(f'Unable to parse year "{text}"', entry)

    try:
        year = int(text[:4])
    except ValueError:
        raise ParseError(f'Unable to parse year "{text}"', entry)
    if year < 1950 or year > 2050:
        raise ParseError('Unlikely year found: {year}', entry)

    return year, letter


def load_models(warnings=True):
    """
    Parses the README file and returns a list of model objects.
    """
    import os
    import re

    def warn(text):
        if warnings:
            print('Warning:', text)

    # Compile regex
    rhead = re.compile(_rhead)
    rbase = re.compile(_rbase)
    rlink = re.compile(_rlink)

    # Find file in root of project
    path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', '..', PATH))
    with open(path, 'r') as f:
        text = f.read()

    # Find start of model list
    try:
        text = text[text.index(f'\n## {FIRST}'):]
    except ValueError:
        raise ParseError('Unable to find first model "{FIRST}"')

    # Split into model entries
    models = {}
    for entry in text.split('\n##')[1:]:
        entry = entry.strip().split('\n')

        # Get year, first author, model type
        m = rhead.fullmatch(entry[0])
        if m is None:
            hint = ''
            if len(entry[0]) > 0 and entry[0][0] not in '12':
                hint = ', expected format: Year Author Type'
            raise ParseError(
                f'Unable to parse header "{entry[0]}"{hint}', entry)
        year, letter = _parse_year(m.group(1), entry)
        model = Model(m.group(2), year, m.group(3), letter)
        models[model.key] = model

        # Get bases
        i = 1
        if len(entry) == i:
            continue
        if not entry[i].startswith('Base:'):
            print(f'Warning: Missing base for {model}')
        else:
            for base in entry[i][5:].split(','):
                base = base.strip()
                m = rbase.match(base)
                if m is None:
                    # Link but not recognised as base? Try giving hints
                    m = rlink.match(base)
                    if m is not None:
                        hint = ''
                        title = m.group(1)
                        if len(title.split(' ')) > 2:
                            hint = ', species and cell type should not be' \
                                   f' included in link title "{m.group(1)}"'
                        elif title[0] in '12':
                            hint = ', title format should be Author Year'
                        else:
                            link = m.group(2)
                            if len(link) > 1 and link[1] not in '12':
                                hint = \
                                    ', link format should be #year-author-type'
                        raise ParseError(
                            f'Unable to parse base: {base}{hint}', entry)
                    continue

                # Check link is local
                if m.group(3) == '':
                    raise ParseError(f'Missing # in base link: {base}', entry)

                # Store link, check later
                model.bases.append(m.group(4))

        # No more info?
        i += 1
        if i >= len(entry):
            continue

        # Get structured data
        fields = set()
        while entry[i].startswith('| '):
            line = entry[i][2:]
            m = rlink.match(line)
            if m is None:
                print('Warning: Unstructured entry after pipe (|):')
                print('  |', line)
            else:
                field, url = m.group(1), m.group(2)
                try:
                    field = _struct[field]
                except KeyError:
                    k, d = _didyoumean(field, _struct)
                    close = f', did you mean "{k}"?' if d < 5 else ''
                    raise ParseError(
                        f'Unhandled structured entry: "{field}"{close}', entry)
                if field in fields:
                    raise ParseError(
                        f'Duplicate structured entry: "{field}"', entry)

                # Check PMR links are up to date
                if 'models.cellml.org' in url:
                    raise ParseError('PMR link using cellml.org instead of'
                                     f' physiomeproject.org: {url}', entry)
                if url.startswith('http://models.physiomeproject'):
                    raise ParseError(
                        f'PMR link using http instead of https: {url}', entry)

                # Store reimplementations in array, rest as property
                if field.startswith('re_'):
                    getattr(model, field).append(url)
                else:
                    getattr(model, field)  # Check exists
                    setattr(model, field, url)

            i += 1
            if i >= len(entry):
                break
        del fields

        # Scan remaining entries
        for i in range(i, len(entry)):
            if entry[i].startswith('|'):
                warn('Possible structured entry following unstructured text:\n'
                     + entry[i])
            if entry[i].startswith('Base:'):
                raise ParseError(
                    'Base should always be first line after title', entry)

    # Check bases given by models
    for model in models.values():
        for base in model.bases:
            if base not in models:
                k, d = _didyoumean(base, models)
                close = f', did you mean {k}?' if d < 5 else ''
                raise ParseError(
                    f'Unknown base: {base} set for {model}{close}')
        model.bases = [models[base] for base in model.bases]

    return list(models.values())

