#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt

import plotstyle as ps

q_wn, wn_sin, wn_sn, a_sin, a_sn, a_0 = np.loadtxt(
                        'data-fig1ab.txt', delimiter=',', skiprows=1, unpack=1)

q_cp, cp_sin, cp_sn = np.loadtxt('data-fig1c.txt', delimiter=',', skiprows=1, unpack=1)


plt.figure()
line_wn_sin = plt.plot(q_wn, wn_sin/1e8, 'r--', **ps.LINESTYLE)
line_wn_sn = plt.plot(q_wn, wn_sn/1e8, 'k-', **ps.LINESTYLE)
plt.xlabel('q, temperature', **ps.LABELSTYLE)
plt.ylabel('Wave number, $10^8$ m$^{-1}$', **ps.LABELSTYLE)

plt.xticks(**ps.TICKSTYLE)
plt.yticks(**ps.TICKSTYLE)
ps.set_tick_style(plt.gcf())

plt.savefig('gpinit-wn.pdf')

plt.figure()
line_a_sin = plt.plot(q_wn, a_sin, 'r--', **ps.LINESTYLE)
line_a_sn = plt.plot(q_wn, a_sn, 'k-', **ps.LINESTYLE)
line_a_0 = plt.plot(q_wn, a_0, 'b--', **ps.LINESTYLE)
plt.xlabel('q, temperature', **ps.LABELSTYLE)
plt.ylabel('$P_0, |P_k P_{-k}|^{0.5}$, C m$^{-2}$', **ps.LABELSTYLE)

plt.xticks(**ps.TICKSTYLE)
plt.yticks(**ps.TICKSTYLE)
ps.set_tick_style(plt.gcf())

plt.subplots_adjust(left=0.15)
plt.savefig('gpinit-a.pdf')

plt.figure()
line_cp_sin = plt.plot(q_cp, cp_sin/1.0e6, 'r--', **ps.LINESTYLE)
line_cp_sn = plt.plot(q_cp, cp_sn/1.0e6, 'k-', **ps.LINESTYLE)
plt.xlabel('q, temperature', **ps.LABELSTYLE)
plt.ylabel('$\Delta C_p$, 10$^6$ J / (K*m$^3$)', **ps.LABELSTYLE)

plt.xticks(**ps.TICKSTYLE)
plt.yticks(**ps.TICKSTYLE)
ps.set_tick_style(plt.gcf())

plt.subplots_adjust(left=0.15)
plt.savefig('gpinit-cp.pdf')
plt.show()