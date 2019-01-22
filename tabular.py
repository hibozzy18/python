from __future__ import print_function
import sys
import pylab as pl
import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt

xval = [x for x in pl.frange(-5.0, 5.0, 0.1)]
if(len(sys.argv) == 2):
    option = sys.argv[1]
    if(int(option) == 1):
        yval = [x for x in xval]
    elif(int(option) == 2):
        yval = [x**2 for x in xval]
    elif(int(option) == 3):
        yval = [x**3 for x in xval]


else:
    print(""""
    Wrong argument list!!. 
    Usage: Tabulation.py N  where is option number.\n
    N has the following options:
    1 ---   f(x)\t  2 ---   f(x**2) \t 3 ---f(x**3)

    """)
    sys.exit(1)

plt.plot(xval, yval)
plt.show()
