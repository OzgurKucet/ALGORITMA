# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 00:00:44 2020

@author: Ozgur Kucet
"""


def f(x):
    return(-2*x**3+12*x*x-20*x+8.5)

x0 = 0
x1 = 4
y0 = -2
h = 1

while(x0<x1):
    y0p = y0 + f(x0)*h
    y0 = y0 + (f(x0)+f(x0+h))*h/2
    x0 += h
    print(y0)
