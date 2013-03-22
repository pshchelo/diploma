#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt

import plotstyle as ps

q_wn, wn_sin, wn_sn = np.loadtxt(
    'data-fig6.txt', delimiter=',', skiprows=1, unpack=1)

line_wn_sin = plt.plot(q_wn, wn_sin, 'r--', **ps.LINESTYLE)
line_wn_sn = plt.plot(q_wn, wn_sn, 'k-', **ps.LINESTYLE)
plt.xlabel('q, temperature', **ps.LABELSTYLE)
plt.ylabel('Wave number', **ps.LABELSTYLE)

plt.xticks(**ps.TICKSTYLE)
plt.yticks(**ps.TICKSTYLE)
ps.set_tick_style(plt.gcf())


plt.savefig('g_3-wn.pdf')

plt.show()
