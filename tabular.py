from __future__ import print_function
import sys
import pylab as pl
import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt
import numpy as np

xval = [x for x in pl.frange(-5.0, 5.0, 0.1)]
if(len(sys.argv) == 2):
    option = sys.argv[1]
    if(int(option) == 1):
        yval = [x for x in xval]
    elif(int(option) == 2):
        yval = [np.exp(x) for x in xval]

    elif(int(option) == 3):
        yval = [np.sqrt(abs(x)) for x in xval]
else:
    print(""""
    Wrong argument list!!. 
    Usage:Tabulation.py N where N is a number between from 1 to 8 inclusive.\n
    N has the following options:
    1 ---f(x)\t  2---exp(x) \t 3 ---sqrt(|x|))

    """)
    sys.exit(1)

plt.plot(xval, yval)
plt.show()
