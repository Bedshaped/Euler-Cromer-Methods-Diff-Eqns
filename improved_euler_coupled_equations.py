# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:10:43 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt

# Defining function

def dxdt(t, x, y):
    return y

def dydt(t, x, y):
    return -x

# Parameters

h = np.pi/100
ncycles = 5
t_max = ncycles*2*np.pi
n = int(t_max/h)

# Initial conditions

x = np.zeros(n)
y = np.zeros(n)

x[0] = 0
y[0] = 1

# Loop and initialize our initial values

t = np.linspace(0, t_max, n)

for i in range(n-1):
    
    c1x = h*dxdt(t[i], x[i], y[i])
    c1y = h*dydt(t[i], x[i], y[i])
    
    x[i + 1] = x[i] + c1x
    y[i + 1] = y[i] + c1y
    
    c2x = h*dxdt(t[i] + h, x[i + 1], y[i + 1])
    c2y = h*dydt(t[i] + h, x[i + 1], y[i + 1])
    
    x[i + 1] = x[i] + 0.5*(c1x + c2x)
    y[i + 1] = y[i] + 0.5*(c1y + c2y)

# Initialize the plot
    
plt.figure(1, figsize=(9, 6))
plt.plot(t, x, label=r"$\~x - \~x(0) = %d$" % x[0])
plt.plot(t, y, label=r"$\~y - \~y(0) = %d$" % y[0])
#plt.plot(t, x + y, label=r"$\~x + \~y$", ls="--")
plt.xlabel("Time")
plt.hlines
plt.legend()