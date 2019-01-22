from __future__ import print_function
import sys

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib import pylab as pl
import numpy as np

xval = [x for x in pl.frange(-3.0, 3.0, 0.1)]
if(len(sys.argv) == 2):
    option = sys.argv[1]
    if(int(option) == 1):
        yval = [x for x in xval]
    elif(int(option) == 2):
        yval = [x**2 for x in xval]
    elif(int(option) == 3):
        yval = [x**3 for x in xval]
    elif(int(option) == 4):
        yval = [np.sin(x) for x in xval]
    elif(int(option) == 5):
        yval = [np.cos(x) for x in xval]
    elif(int(option) == 6):
        yval = [np.tan(x) for x in xval]
    elif(int(option) == 7):      
        yval = [np.exp(x) for x in xval]
    elif(int(option) == 8):
        yval = [np.sqrt(abs(x)) for x in xval]
else:
    print(""""
    Wrong argument list!!. 
    Usage:Tabulation.py N where N is a number between from 1 to 8 inclusive.\n
    N has the following options:
    1 ---   f(x)\t  2 ---   f(x**2) \t 3 ---f(x**3) \t 4 ---sin(x) 
    5 --- cos(x)\t  6 --- tan(x**2) \t 7 ---exp(x) \t 8 ---sqrt(|x|))

    """)
    sys.exit(1)

plt.plot(xval, yval)
plt.show()
