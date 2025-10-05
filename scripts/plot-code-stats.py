#!/usr/bin/env python
#
# Plots (1) the code type models were published with, over time and (2) the
# fraction in PMR over time
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


def save(fig, name):
    print(f'Saving to {name}.png and .svg')
    fig.savefig(f'{name}.png', dpi=120)
    fig.savefig(f'{name}.svg')


#
# Plot code type accompanying publications
#
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
sums['none'] = np.cumsum(nocode)
format_codes = dict(format_codes)
format_codes['none'] = 'None'

# Count total, before 'other' etc are added
ntot = sum(v[-1] for v in sums.values())

# Get formats, ordered by count
keys = [x[0] for x in sorted(sums.items(), key=lambda x: -x[1][-1])]

# Show at most npop?
npop = 5
colors = plt.get_cmap('tab10').colors
if len(keys) > npop:
    sums['other'] = np.copy(sums[keys[npop]])
    for i in range(npop + 1, len(keys)):
        sums['other'] += sums[keys[i]]
    keys2 = [keys[i] for i in range(1 + npop)]
    keys2[npop] = 'other'
    format_codes['other'] = 'Other'

#
# 1. Show npop most used
#
fig = plt.figure(figsize=(9, 4.6))
fig.subplots_adjust(0.065, 0.095, 0.94, 0.985)
ax = fig.add_subplot()
ax.set_xlabel('Models published to date')
ax.set_ylabel('Number with author-provided code (lower bound)')

# Plot cumulative counts, stacked on top of each other. For most popular
alpha = 0.2
zorders = 1 + np.arange(len(keys2))
zorders = zorders[::-1]
colors = [colors[i] for i in range(len(keys2))]
lower = np.zeros(years.shape)
for f, c, z in zip(keys2, colors, zorders):
    upper = lower + sums[f]
    ax.fill_between(years, lower, upper, color=lumen(c, alpha))
    ax.plot(years, upper, label=format_codes[f], color=c, zorder=z)
    lower = upper
ax.legend(loc=(0.025, 0.4), frameon=False, reverse=True)
ax.set_ylim(0, 261)
ax.set_xlim(2000, y1 - 1)

y = 0
for f in keys2[:6]:
    y += sums[f][-1]
    p = 100 * sums[f][-1] / ntot
    ax.text(y1 - 0.85, y, f'{p:.1f}%', va='center')
ax.spines[['right', 'top']].set_visible(False)
save(fig, 'format-vs-model-date')


#
# 2. Show as percentage
#
fig = plt.figure(figsize=(9, 4.6))
fig.subplots_adjust(0.065, 0.095, 0.87, 0.985)
ax = fig.add_subplot()
ax.set_xlabel('Models published to date')
ax.set_ylabel('Percentage with author-provided code (lower bound)')

# Plot cumulative counts, stacked on top of each other. For most popular
alpha = 0.2
zorders = 1 + np.arange(len(keys2))
zorders = zorders[::-1]
colors = [colors[i] for i in range(len(keys2))]
total = np.sum([sums[f] for f in keys2], axis=0) * 0.01
lower = np.zeros(years.shape)
for f, c, z in zip(keys2, colors, zorders):
    upper = lower + sums[f]
    ax.fill_between(years, lower / total, upper / total, color=lumen(c, alpha))
    ax.plot(years, upper / total, label=format_codes[f], color=c, zorder=z)
    lower = upper
ax.set_ylim(0, 101)
ax.set_xlim(2000, y1 - 1)

y = 0
for f in keys2[:6]:
    p = 100 * sums[f][-1] / ntot
    y += p
    ax.text(y1 - 0.85, y, f'{f} ({p:.1f}%)', va='center')
    ax.text(p, 1, 'Hello')
ax.spines[['right', 'top']].set_visible(False)
save(fig, 'format-vs-model-date-percentage')


#
# 3. Focus on lesser used formats
#
nskip = 3

fig = plt.figure(figsize=(9, 4.6))
fig.subplots_adjust(0.065, 0.095, 0.94, 0.985)
ax = fig.add_subplot()
ax.set_xlabel('Models published to date')
ax.set_ylabel('Number with author-provided code (lower bound)')

keys = keys[nskip:]
zorders = 1 + np.arange(len(keys))
zorders = zorders[::-1]
colors = plt.get_cmap('tab20').colors
colors = colors[0::2] + colors[1::2]
colors = [colors[i] for i in range(nskip, nskip + len(keys))]
lower = np.zeros(years.shape)
for f, c, z in zip(keys, colors, zorders):
    upper = lower + sums[f]
    ax.fill_between(years, lower, upper, color=lumen(c, alpha))
    ax.plot(years, upper, label=format_codes[f], color=c, zorder=z)
    lower = upper
ax.legend(loc=(0.025, 0.4), frameon=False, reverse=True)
ax.set_ylim(0, 46)
ax.set_xlim(2000, y1 - 1)

y = 0
for f in keys:
    y += sums[f][-1]
    p = 100 * sums[f][-1] / ntot
    ax.text(y1 - 0.85, y, f'{p:.1f}%', va='center')
ax.spines[['right', 'top']].set_visible(False)
save(fig, 'format-vs-model-date-zoom')

#
# 4. Relational vs procedural
#
pro, rel = np.zeros(years.shape), np.zeros(years.shape)
keys = list(sums.keys())
for key in keys:
    if key in ('none', 'other'):
        continue
    elif key in ('cellml', 'myokit'):
        rel += sums[key]
    else:
        pro += sums[key]

show = {
    'None': sums['none'],
    'Procedural': pro,
    'Declarative': rel,
}

fig = plt.figure(figsize=(9, 4.6))
fig.subplots_adjust(0.065, 0.095, 0.94, 0.985)
ax = fig.add_subplot()
ax.set_xlabel('Models published to date')
ax.set_ylabel('Number with author-provided code (lower bound)')

keys = keys[nskip:]
zorders = 1 + np.arange(len(keys))
zorders = zorders[::-1]
colors = plt.get_cmap('tab20').colors
colors = colors[0::2] + colors[1::2]
colors = [colors[i] for i in range(len(keys))]
lower = np.zeros(years.shape)
for k, s, c, z in zip(show.keys(), show.values(), colors, zorders):
    upper = lower + s
    ax.fill_between(years, lower, upper, color=lumen(c, alpha))
    ax.plot(years, upper, label=k, color=c, zorder=z)
    lower = upper
ax.legend(loc=(0.025, 0.6), frameon=False, reverse=True)
ax.set_ylim(0, 261)
ax.set_xlim(2000, y1 - 1)

y = 0
for k, s in show.items():
    y += s[-1]
    p = 100 * s[-1] / ntot
    ax.text(y1 - 0.85, y, f'{p:.1f}%', va='center')
ax.spines[['right', 'top']].set_visible(False)
save(fig, 'format-vs-model-date-type')


#
# 5. Relational vs procedural - as a percentage
#
fig = plt.figure(figsize=(9, 4.6))
fig.subplots_adjust(0.065, 0.095, 0.835, 0.985)
ax = fig.add_subplot()
ax.set_xlabel('Models published to date')
ax.set_ylabel('Percentage with author-provided code (lower bound)')

total = np.sum([s for s in show.values()], axis=0) * 0.01
for k, s, c, z in zip(show.keys(), show.values(), colors, zorders):
    ax.plot(years, s / total, label=k, color=c, zorder=z)
    lower = upper

ax.set_ylim(0, 101)
ax.set_xlim(2000, y1 - 1)
for k, s in show.items():
    p = 100 * s[-1] / ntot
    ax.text(y1 - 0.85, p, f'{k} ({p:.1f}%)', va='center')
ax.spines[['right', 'top']].set_visible(False)
save(fig, 'format-vs-model-date-type-percentage')

ax.plot(years, sums['cellml'] / total, label='CellML', color=colors[2],
        zorder=0, ls='--')
p = 100 * sums['cellml'][-1] / ntot
ax.text(y1 - 0.85, p, f'CellML ({p:.1f}%)', va='center')
save(fig, 'format-vs-model-date-type-percentage-cellml')


#
# 6. Plot percentage in PMR - far larger number than published with CellML
#
fig = plt.figure(figsize=(9, 4.1))
fig.subplots_adjust(0.070, 0.105, 0.955, 0.985)
ax = fig.add_subplot()
ax.set_xlabel('Models published to date')
ax.set_ylabel('Percentage in PMR (upper bound)')
ax.secondary_yaxis('right')
n_out, n_pmr = np.zeros(years.shape), np.zeros(years.shape)
for m in models:
    n_out[m.year - y0] += 1
    n_pmr[m.year - y0] += (1 if m.in_pmr() else 0)
n_out, n_pmr = np.cumsum(n_out), np.cumsum(n_pmr)

lower = np.zeros(years.shape)
perce = 100 * n_pmr / n_out
upper = np.ones(years.shape) * 100

colors, i = plt.get_cmap('tab10').colors, 3
ax.fill_between(years, lower, perce, color=lumen(colors[i], .2))
ax.fill_between(years, upper, perce, color='#eee')
ax.plot(years, perce, color=colors[i])
ax.set_xlim(y0, y1 - 1)
ax.set_ylim(0, 101)

ax.spines[['top']].set_visible(False)
save(fig, 'percentage-in-pmr')
ax.set_xlim(2000, y1 - 1)
save(fig, 'percentage-in-pmr-zoom')
print('done')
