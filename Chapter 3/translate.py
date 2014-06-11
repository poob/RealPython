'''
Created on Jun 9, 2014

@author: Poob
'''
# This program will turn any string into "l33t h4x04" format

input = raw_input("Enter some text for transform:")

input = input.replace('a', '4')
input = input.replace('b', '8')
input = input.replace('e', '3')
input = input.replace('l', '1')
input = input.replace('o', '0')
input = input.replace('s', '5')
input = input.replace('t', '7')

print input