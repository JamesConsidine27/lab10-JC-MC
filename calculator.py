"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
# https://github.com/JamesConsidine27/lab10-JC-MC
# Partner 1: James Considine
# Partner 2: Matias Christensen
import math

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("log domain error")
    return math.log(b, a)

def exp(a, b):
    return a ** b





