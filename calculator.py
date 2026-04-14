"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero.")
    
    return a / b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1")
    
    if b <= 0:
        raise ValueError("Argument b must be positive.")
    
    return math.log(a, b)

def exponent(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)


    

