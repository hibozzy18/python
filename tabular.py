import sys
import pylab as pl

xval = [x for x in pl.frange(-5.0, 5.0, 0.1)]
if(len(sys.argv) == 2):
    option = sys.argv[1]
    if(int(option) == 1):
        yval = [x for x in xval]
