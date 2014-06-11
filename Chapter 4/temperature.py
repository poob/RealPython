'''
Created on Jun 10, 2014

@author: Poob
'''
from __future__ import division

def convertCtoF(c):
    f = c * 9 / 5 + 32
    return float(f)

def convertFtoC(f):
    c = (f - 32) * 5 / 9
    return c

f = 72
c = 37
print "{} degrees F = {} degrees C".format(f, convertFtoC(f))
print "{} degrees C = {} degrees F".format(c, convertCtoF(c))