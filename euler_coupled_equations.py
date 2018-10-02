# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:11:00 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt

# Defining function

def dxdt(t, y):
    return y

def dydt(t, x):
    return -x

# Parameters

h = np.pi/1000
ncycles = 5
t_max = ncycles*2*np.pi
n = int(t_max/h)

# Initial conditions

x = np.zeros(n)
y = np.zeros(n)

x[0], y[0] = 0, 1

# Loop and initialize our initial values

t = np.linspace(0, t_max, n)

for i in range(n-1):
    x[i + 1] = x[i] + h*dxdt(t[i], y[i])
    y[i + 1] = y[i] + h*dydt(t[i], x[i])

# Initialize the plot
    
plt.figure(1, figsize=(9, 6))
plt.plot(t, x, label=r"$\~x - \~x(0) = %d$" % x[0])
plt.plot(t, y, label=r"$\~y - \~y(0) = %d$" % y[0])
plt.xlabel("Time")
plt.legend()
