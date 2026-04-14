# https://github.com/Edison-LaraBojay/LAB11-ELB-LO.git
# Partner 1: Edison Lara-Bojay
# Partner 2: Lucas Ocano

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example


import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base")
    if b <= 0:
        raise ValueError("Invalid argument")
    return math.log(b, a)

def exp(a, b):
    return a ** b


def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1")
    
    if b <= 0:
        raise ValueError("Argument b must be positive.")
    
    return math.log(b, a)

def exponent(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)



