# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:32:13 2020

@author: Administrator
"""

#title deep neural netw.


def fp(input):
        
        l1 = 1/(1+exp(-dot(input,w0)))
        l2 = 1/(1+exp(-dot(l1,w1)))
        return l1,l2
    
def bp(l1, l2, y):
    error = y - l2
    slope = l2*(1-l2)
    l1_delta = error*slope
    l0_slope = l1*(1-l1)
    l0_error = l1_delta.dot(w1.T)
    l0_delta = l0_slope*l0_error
    return l0_delta, l1_delta

    
from numpy import random, dot, exp, array
X = array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
y = array([[0,1,1,0]]).T

random.seed(1)
w0 = random.random((3,20)) * 2 - 1
w1 = random.random((20,1)) * 2 - 1

for i in range(10000):
    l0 = X
    l1,l2 = fp(l0)
    l0_delta , l1_delta = bp(l1, l2, y)

    
    w1 = w1 + dot(l1.T, l1_delta)
    w0 = w0 + dot(l0.T, l0_delta)

print(fp([[0,0,0]])[1])