# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:13:08 2020

@author: Administrator
"""

from numpy import random, dot, exp, array
X = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
y = array([[0,1,1,0]]).T

random.seed(1)
weights = 2*random.random((3,1))-1

for i in range(5000000):
    z=dot(X,weights)
    output=1/(1+exp(-z))
    error = y - output
    slope = output*(1-output)
    delta = error * slope
    weights = weights + dot(X.T, delta)
    

print(weights)