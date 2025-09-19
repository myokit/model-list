#!/usr/bin/env python
#
# Plots the number of models in PMR, and who added them
#
import colorsys
import sys

import numpy as np
import matplotlib.pyplot as plt


path = 'pmr-stats-20250918.csv'
stacked = True


def lumen(color, scale):
    """ Scale a color's lightness. """
    h, l, s = colorsys.rgb_to_hls(*color)
    return colorsys.hls_to_rgb(h, min(1, 1 - l * scale), s)


# Load data
rows = np.genfromtxt(path, delimiter=',', names=True, dtype=None)
for row in rows:
    # Chop off quotes
    row[2] = row[2][1:-1]

# Check types
mtypes = ('Curator', 'Author', 'Third party')
error = False
for row in rows:
    if row[2] not in mtypes:
        print('Unknown type:', row)
        error = True
if error:
    sys.exit(1)

# Get years added, by type
years = [row[1] for row in rows]
y0, y1 = min(years), max(years) + 1
years = np.arange(y0, y1)
counts = [np.zeros(years.shape) for x in mtypes]
for row in rows:
    counts[mtypes.index(row[2])][row[1] - y0] += 1

# Get total in db, per year
totals = [np.cumsum(x) for x in counts]
combined = np.sum(totals, axis=0, dtype=int)

#
# 1. Total
#
fig = plt.figure(figsize=(9, 4.1))
ax = fig.add_subplot()
ax.set_xlabel('Year added (approximate)')
ax.set_ylabel('Total number of CCE models in PMR')
if stacked:
    alpha = 0.2
    fig.subplots_adjust(0.065, 0.105, 0.99, 0.99)
    ax.fill_between(years, combined, color='#e9e9e9')
    ax.plot(years, combined, 'k')
    ax.set_xlim(y0, y1 + 2)
    ax.set_ylim(0, 110)
else:
    fig.subplots_adjust(0.065, 0.105, 0.98, 0.99)
    ax.plot(years, combined)
    ax.set_xlim(y0, y1)
ax.text(y1 - 0.7, combined[-1], combined[-1], va='center')
ax.spines[['right', 'top']].set_visible(False)
fig.savefig('total-vs-pmr-date.png', dpi=120)
fig.savefig('total-vs-pmr-date.svg')


#
# 2. Split per type
#
colors = plt.get_cmap('tab10').colors
colors = [colors[i] for i in range(len(mtypes))]

# Plot cumulative counts, stacked on top of each other
fig = plt.figure(figsize=(9, 4.1))
ax = fig.add_subplot()
ax.set_xlabel('Year added (approximate)')
ax.set_ylabel('Total number of CCE models in PMR')
if stacked:
    fig.subplots_adjust(0.065, 0.105, 0.99, 0.99)
    zorders = 1 + np.arange(len(mtypes))
    zorders = zorders[::-1]
    lower = np.zeros(years.shape)
    for author, count, color, zorder in zip(mtypes, totals, colors, zorders):
        upper = lower + count
        ax.fill_between(years, lower, upper, color=lumen(color, alpha))
        ax.plot(years, upper, color=color, zorder=zorder)
        ax.text(y1 - 0.7, upper[-1], author, va='center')
        lower = upper
    ax.set_xlim(y0, y1 + 2)
    ax.set_ylim(0, 110)
else:
    fig.subplots_adjust(0.055, 0.105, 0.99, 0.99)
    for author, count in zip(mtypes, totals):
        ax.plot(years, count, label=author)
    ax.set_xlim(y0, y1 + 2)
    ax.set_ylim(0, 75)
    for total, author in zip(totals, mtypes):
        ax.text(y1 - 0.7, total[-1], mtypes[i], va='center')
ax.spines[['right', 'top']].set_visible(False)
fig.savefig('total-vs-pmr-date-by-author.png', dpi=120)
fig.savefig('total-vs-pmr-date-by-author.svg')

print('done')

