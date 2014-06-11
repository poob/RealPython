'''
Created on Jun 9, 2014

@author: Poob
'''
import unittest

myString = "AAA"
print myString.find('a')
# -1

version = "version 2.0"
num = 2.0
print version.find(str(num))

input = raw_input("What is your string?")
letter = raw_input("What letter do you want to find in your string?")
print input.find(letter)