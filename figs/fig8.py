#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt

import plotstyle as ps

q_cpt, cpt_sin, cpt_sn = np.loadtxt(
    'data-fig8.txt', delimiter=',', skiprows=1, unpack=1)

line_cpt_sin = plt.plot(q_cpt, cpt_sin, 'r--', **ps.LINESTYLE)
line_cpt_sn = plt.plot(q_cpt, cpt_sn, 'k-', **ps.LINESTYLE)
plt.xlabel('q, temperature', **ps.LABELSTYLE)
plt.ylabel('$\Delta C_p / T$', **ps.LABELSTYLE)

plt.xticks(**ps.TICKSTYLE)
plt.yticks(**ps.TICKSTYLE)
ps.set_tick_style(plt.gcf())


plt.savefig('g_3-cpt.pdf')

plt.show()
