from __future__ import print_function
import sys
import pylab as pl
import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt

xval = [x for x in pl.frange(-3.0, 3.0, 0.1)]
if(len(sys.argv) == 2):
    option = sys.argv[1]
    if(int(option) == 1):
        yval = [x for x in xval]

else:
    print(""""
    Wrong argument list!!. 
    Usage: Tabulation.py N  where is option number.\n
    N has the following options:
    1 ---   f(x)\t 

    """)
    sys.exit(1)

plt.plot(xval, yval)
plt.show()
