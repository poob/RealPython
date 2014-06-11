'''
Created on Jun 9, 2014

@author: Poob
'''

s1 = "abra"
s2 = "cadabra"
s3 = s1 + s2
print s3
# abracadabra

s4 = "abra" + "cadabra"
print s4
# abracadabra

print "abra", "ca", "dabra" # abra ca dabra

flavor = "birthday cake"
print flavor[3]
# t

print flavor[0:3]
# bir

print flavor[:5]
# birth

print flavor[5:]
#day cake

print flavor[:]
# birthday cake

# ---------------------------
# Python String are immutable
# ---------------------------
myString = "goal"
myString = "G" + myString[1:]
print myString
# Goal

myString = "goal"
myString[0] = "G" # this won't work at runtime
