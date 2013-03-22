import matplotlib as mpl

mpl.rcParams['axes.linewidth'] = 2
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['figure.subplot.bottom'] = 0.12
mpl.rcParams['figure.subplot.top'] = 0.95
mpl.rcParams['figure.subplot.right'] = 0.95

LINESTYLE = {
            'linewidth':3,
            'markersize':7,
            }
LABELSTYLE = {
            'size':20,
            'labelpad':10
            }

MATHSTYLE = {
            'size':28,
            'weight':'bold',
            }

TITLESTYLE = {
            'size':22,
            'weight':'bold',
            }

TICKSTYLE = {
            'size':18,
            }

LEGENDSTYLE = {
            'size':16,
            }

TICKLINESTYLE={
            'markersize':10,
            'markeredgewidth':2,
            }

def set_tick_style(fig):
    for ax in fig.get_axes():
        for tick in ax.get_xticklines()+ax.get_yticklines():
            tick.set(**TICKLINESTYLE)
