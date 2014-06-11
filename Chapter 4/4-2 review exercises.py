'''
Created on Jun 9, 2014

@author: Poob
'''
#
# Functions
#
def square(number):
    """
    Returns the result of number raised to the power of two
    """
    result = number ** 2
    return result

def returnDifference(num1, num2):
    """
    Return the difference between two numbers.
    Subtracts n2 from n1.
    """
    return num1 - num2

def cube(number):
    """
    Return the result of number raised to the power of three
    """
    result = number * number * number
    return result

def multiply(num1, num2):
    """
    Return the result of mutiplying num1 with num2
    """
    result = num1 * num2
    return result

input = 5
result = square(input)
print result
# 25
print returnDifference(3, 5)
# -2

help(returnDifference)

print cube(3)
print multiply(1, 2)