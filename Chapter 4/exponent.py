'''
Created on Jun 9, 2014

@author: Poob
'''
base = raw_input("Enter a base: ")
base = float(base)
exponent = raw_input("Enter an exponent: ")
exponent = float(exponent)
result = base ** exponent
print "{} to the power of {} = {}".format(base, exponent, result)