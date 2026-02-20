# Figures

Based on the model list (see [here](../README.md) for details of model selection), we can create graphs showing the number of models published over time and the formats the code was published in (if any).

The figure below shows the cumulative number of models with author-provided code from 2000 onwards, split by format the code was published in, or "None" if no code could be found online.

![format-vs-model-data](format-vs-model-date.svg)

As this is based on the manually compiled list, the raw numbers on the left y-axis should be interpreted as a lower bound.
Once a model is known, a targetted search for accompanying code was performed (looking in papers, lab websites, model repositories, and search engines), so that the percentages on the right y-axis are most likely a good approximation.

Another caveat is that code may have been published in other ways, e.g. mailed or emailed before online dissemination became the norm, or may have been removed since online publication.
For this reason, we chose 2000 as the earliest included date.

The "other" category can be split up to reveal the smaller (less than 5%) players:

![format-vs-model-data-zoom](format-vs-model-date-zoom.svg)

Note that C and C++ combined make up 5.7% here, and most of the published C++ models make limited use of the extra features found in C++ versus C.

