import math
def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    return a / b

def log(a, b):
    if b <= 0:
        raise ValueError("Base must be greater than 1")
    if a <= 0:
        raise ValueError("Input value must be greater than 0")
    return math.log(a, b)

def square(a):
    return a ** 2

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def square_root(a):
    if a < 0:
        raise ValueError("Cannot square root negative number")
    return math.sqrt(a)

def percentage(a, b):
    if b <= 0:
        raise ValueError("Total must be greater than 0")
    return (a / b) * 100





