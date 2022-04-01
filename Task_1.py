# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 22:11:12 2022

@author: joyce
"""

# Assignment 1

#______________________________________________________________________________
# Task 1 & 2
import math as m

def newton_exact(x_0):
    f = m.atan(x_0)
    df = 1/(1+x_0**2)
    x_1 = x_0 - f/df
    return x_1

def newton_approx(x_0):
    h = 0.01
    f = m.atan(x_0)
    f_h = m.atan(x_0 + h)
    df = (f_h - f)/h
    if df == 0:
        x_1 = x_0
    else:
        x_1 = x_0 - f/df
    return x_1

def secant(x_0, x_1):
    f_0 = m.atan(x_0)
    f_1 = m.atan(x_1)
    if f_0 == f_1: 
        x_2 = x_0
    else:
        x_2 = x_1 - f_1*((x_1-x_0)/(f_1-f_0))
    return x_2

iterations = 30
x_init = -2.33
x_init_1 = 2.28

'''
# Newton method with exact derivative 
value = []
x = x_init
for i in range (0, iterations):
    x = newton_exact(x)
    value.append(x)
print(value)
print('\n')
'''
'''
# Newton method with finite differences approximation of derivative
value = []
x = x_init
for i in range (0, iterations):
    x = newton_approx(x)
    value.append(x)
print(value)
print('\n')
'''
'''
# Secant method
value = []
x_0 = x_init
x_1 = x_init_1
for i in range (0, iterations):
    x_2 = secant(x_0, x_1)
    x_0 = x_1
    x_1 = x_2
    value.append(x_2)
print(value)
'''

#______________________________________________________________________________
# Task 3

def logistic(x, alpha):
    f = alpha*x*(1-x)
    return f

def fixed_point_it(x_0, alpha):
    x_1 = x_0 + logistic(x_0, alpha)
    return x_1

x_0 = 1.1
alpha = 3.3
iterations = 20
values = []

for i in range(0, iterations):
    x_1 = fixed_point_it(x_0, alpha)
    values.append(x_1)
    x_0 = x_1
print(values)
    
#______________________________________________________________________________
# Task 4
'''
from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
solve(sympy.atan(x), 0)
'''