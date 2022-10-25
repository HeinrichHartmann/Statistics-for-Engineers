import math, json, os
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime
import matplotlib as mpl
from matplotlib import pyplot as plt
from scipy import stats
from IPython.display import HTML, display
from collections import *
from math import *

try:
    from tabulate import tabulate
except:
    print("Could not load tabulate")
    
display(HTML("""
<style>
.custom {
    font-size: 18pt;
    font-family: monospace;
}
</style>
"""))

def P(*args):
    display(HTML('<p class="custom">{}</p>'.format(" ".join([ str(a) for a in args ]))))

def H(txt): display(HTML("<h3>{}</h3>".format(txt)))

def TAB(*args, **kwargs): print(tabulate(*args, **kwargs))
    
mpl.rcParams['figure.figsize'] = (20,5)


from circllhist import Circllhist
from circonusapi import circonusdata

with open(os.path.expanduser("~/work/.circonusrc.json"),"r") as fh: 
    config = json.load(fh)

def caql(account, q, start, period, count):
    circ = circonusdata.CirconusData(config[account])
    return circ.caql(q, start, period, count)

def caql_plot(account, q, start, period, count, *args, **kwargs):
    circ = circonusdata.CirconusData(config[account])
    res = circ.caql(q, start, period, count)
    for k,v in res.items(): plt.plot( v, *args, **kwargs )
    return res