# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 02:29:50 2020

@author: Ozgur Kucet
"""


def f(x,y):
    return(-y/x)

x0 = 4
x1 = 7
y0 = 0.75
h = 0.00001

while(x0<x1):
    y0 = y0 + f(x0, y0)*h
    x0 += h

print(y0)