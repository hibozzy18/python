from __future__ import print_function
import sys
import pylab as pl
import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt
import numpy as np

xval = [x for x in pl.frange(-3.0, 3.0, 0.1)]
if(len(sys.argv) == 2):
    option = sys.argv[1]
    if(int(option) == 1):
        yval = [x for x in xval]
    elif(int(option) == 2):
        yval = [np.sin(x) for x in xval]
    elif(int(option) == 3):
        yval = [np.cos(x) for x in xval]
    elif(int(option) == 4):
        yval = [np.tan(x) for x in xval]
        

else:
    print(""""
    Wrong argument list!!. 
    Usage:Tabulation.py N where N is a number between from 1 to 4 inclusive.\n
    N has the following options:
    1 ---   f(x)\t  2---sin(x) 
    3 --- cos(x)\t  4--- tan(x**2) 

    """)
    sys.exit(1)

plt.plot(xval, yval)
plt.show()
