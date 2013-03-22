#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt

import plotstyle as ps

x, k, dk, T = np.loadtxt(
    'data-fig9.txt', delimiter=',', skiprows=1, unpack=1)

barprops = {
        'linestyle': '-',
        'color': 'black',
        'ecolor': 'red',
        'elinewidth': 1,
        'marker': 's',
        'markerfacecolor': 'white',
        'markeredgewidth': 1,
        'markeredgecolor': 'black',
        }

barprops.update(ps.LINESTYLE)
line_wn_exp = plt.errorbar(T, k*1e4, dk*1e4, **barprops)

plt.xlabel('temperature T, K', **ps.LABELSTYLE)
plt.ylabel('Wave vector k, $10^{-4} \AA^{-1}$', **ps.LABELSTYLE)

plt.xticks(**ps.TICKSTYLE)
plt.yticks(**ps.TICKSTYLE)
ps.set_tick_style(plt.gcf())

plt.savefig('exp-wn.pdf')

plt.show()
