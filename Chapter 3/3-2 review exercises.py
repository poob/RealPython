'''
Created on Jun 9, 2014

@author: Poob
'''

weight = 0.2
animal = "newt"
print str(weight) + " kg is the weight of the " + animal

print "{} kg is the weight of the {}".format(weight, animal)
print "{0} kg is the weight of the {1}".format(weight, animal)
print "{float} kg is the weight of the {name}".format(float=0.2, name="newt")
print "{} kg is the weight of the {}".format(0.2, "newt")