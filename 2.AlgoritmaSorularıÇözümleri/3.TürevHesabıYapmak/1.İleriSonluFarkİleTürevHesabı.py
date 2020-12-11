# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:59:21 2020

@author: Ozgur Kucet
"""


def f(x):
    return(x**3+2*x+8)

x0 = 1
h = 1 #1 alırsak normalde  türevi 5 olması lazımken bize 9 veriyor..

xprime = (f(x0+h)-f(x0))/h

print(xprime)