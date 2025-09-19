#!/usr/bin/env python
#
# Plots the code type models were published with, over time
#
import colorsys
import sys

import numpy as np
import matplotlib.pyplot as plt

from shared import (
    load_models,
    ParseError,
    print_parse_error,
    format_codes,
)


stacked = True

try:
    models = load_models()
except ParseError as e:
    print_parse_error(e)
    sys.exit(1)


def lumen(color, scale):
    """ Scale a color's lightness. """
    h, l, s = colorsys.rgb_to_hls(*color)
    return colorsys.hls_to_rgb(h, min(1, 1 - l * scale), s)


fig = plt.figure(figsize=(9, 4.6))
fig.subplots_adjust(0.065, 0.095, 0.98, 0.985)
ax = fig.add_subplot()
ax.set_xlabel('Model publication date')
ax.set_ylabel('Number of models published with code')

# Get number of models published with each format, per year
years = set([m.year for m in models])
y0, y1 = min(years), max(years) + 1
years = np.arange(y0, y1)
counts = {k: np.zeros(years.shape) for k in format_codes}
nocode = np.zeros(years.shape)
for m in models:
    fs = m.author_provided_formats()
    if len(fs) == 0:
        nocode[m.year - y0] += 1
    for f in fs:
        counts[f][m.year - y0] += 1

# Convert to cumulative sums
sums = {k: np.cumsum(v) for k, v in counts.items()}
ncds = np.cumsum(nocode)

# Get formats, ordered by count
keys = [x[0] for x in sorted(sums.items(), key=lambda x: -x[1][-1])]

# Get a colour per format
colors = plt.get_cmap('tab10').colors
colors = [colors[i] for i in range(len(keys) + 1)]
totals = np.zeros(years.shape)

# Plot cumulative counts, stacked on top of each other
if stacked:
    alpha = 0.2
    zorders = 1 + np.arange(len(keys) + 1)
    zorders = zorders[::-1]
    upper = totals + ncds
    ax.fill_between(years, totals, upper, color=lumen(colors[0], alpha))
    ax.plot(years, upper, label='None', color=colors[0], zorder=zorders[0])
    for f, c, z in zip(keys, colors[1:], zorders[1:]):
        totals = upper
        upper = totals + sums[f]
        ax.fill_between(years, totals, upper, color=lumen(c, alpha))
        ax.plot(years, upper, label=format_codes[f], color=c, zorder=z)
    ax.legend(loc=(0.025, 0.4), frameon=False)
else:
    ax.plot(years, ncds, label='None', color=colors[0])
    for f, c in zip(keys, colors[1:]):
        ax.plot(years, sums[f], label=format_codes[f], color=c)
    ax.legend(loc=(0.025, 0.5), frameon=False)

ax.set_xlim(2000, y1 - 1)
ax.spines[['right', 'top']].set_visible(False)
fig.savefig('code-type-vs-model-date.png', dpi=120)
fig.savefig('code-type-vs-model-date.svg')
print('done')

