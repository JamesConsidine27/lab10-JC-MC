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
        raise ZeroDivisionError
    return a / b


def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        return math.log(math.e, b)


def exp(a, b):
    return a ** b





