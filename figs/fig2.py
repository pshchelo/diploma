#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt

import plotstyle as ps

q_wn, wn_sin, wn_sn, a_sin, a_sn, a_0 = np.loadtxt(
                        'data-fig2ab.txt', delimiter=',', skiprows=1, unpack=1)

q_cp, cpt_sin, cpt_sn = np.loadtxt('data-fig2c.txt', delimiter=',', skiprows=1, unpack=1)


plt.figure()
line_wn_sin = plt.plot(q_wn, wn_sin, 'r--', **ps.LINESTYLE)
line_wn_sn = plt.plot(q_wn, wn_sn, 'k-', **ps.LINESTYLE)
plt.xlabel('q, temperature', **ps.LABELSTYLE)
plt.ylabel('Wave number', **ps.LABELSTYLE)

plt.xticks(**ps.TICKSTYLE)
plt.yticks(**ps.TICKSTYLE)
ps.set_tick_style(plt.gcf())

plt.savefig('nogap-wn.pdf')

plt.figure()
line_a_sin = plt.plot(q_wn, a_sin, 'r--', **ps.LINESTYLE)
line_a_sn = plt.plot(q_wn, a_sn, 'k-', **ps.LINESTYLE)
line_a_0 = plt.plot(q_wn, a_0, 'b--', **ps.LINESTYLE)
plt.xlabel('q, temperature', **ps.LABELSTYLE)
plt.ylabel('Amplitude', **ps.LABELSTYLE)

plt.xticks(**ps.TICKSTYLE)
plt.yticks(**ps.TICKSTYLE)
ps.set_tick_style(plt.gcf())

plt.savefig('nogap-a.pdf')

plt.figure()
line_cp_sin = plt.plot(q_cp, cpt_sin, 'r--', **ps.LINESTYLE)
line_cp_sn = plt.plot(q_cp, cpt_sn, 'k-', **ps.LINESTYLE)
plt.xlabel('q, temperature', **ps.LABELSTYLE)
plt.ylabel('$\Delta C_p / T$', **ps.LABELSTYLE)

plt.xticks(**ps.TICKSTYLE)
plt.yticks(**ps.TICKSTYLE)
ps.set_tick_style(plt.gcf())

plt.savefig('nogap-cpt.pdf')
plt.show()