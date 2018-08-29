import math
import numpy as np
import matplotlib as mpl
import seaborn as sns
from matplotlib import pyplot as plt
mpl.rcParams['figure.figsize'] = (15,5)

# A plotting helper for circllhist
from matplotlib import pyplot as plt
def circllhist_plot(H,*,ax=None,mbe = 0, **kwargs):
    mb = 10 ** mbe
    H = H.compress_mbe(mbe)
    if not ax:
        ax = plt.subplot(1,1,1)
    x=[] # midpoints
    h=[] # height
    w=[] # widths
    for b, c in H:
        if b.edge() == 0:
            # 0 bucket, spans -mb ... +mb
            wdt = 2*mb
            x.append(0)
            w.append(wdt)
            h.append(c/wdt)
        elif b.exp == mbe:
            # mbe buckets are scaled by a factor of 10
            sgn = 1 if b.val > 0 else -1
            wdt = b.width() * 10
            mid = b.edge()  + sgn * wdt/2
            x.append(mid)
            w.append(wdt)
            h.append(c/wdt)
        else:
            x.append(b.midpoint())
            w.append(b.width())
            h.append(c/b.width())
    ax.bar(x,h,w,**kwargs)
    ax.set_xlim(-50,50)
    return ax