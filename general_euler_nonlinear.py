# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:54:54 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt

# Defining function

def f(x, t):
    return t - x**2

def differential(x, t, h):
    return x + h*f(x, t)

# Parameters

h = 0.05
t_max = 9
n = int(t_max/h)

# Initial conditions

x = np.zeros(n)
x[0] = 3
t = np.linspace(0, t_max, n)

# Loop

for i in range(n - 1):
    value = differential(x[i + 1], t[i + 1], h)
    x[i + 1] = value


# Deviation of methods
    

# Initialize the plot

plt.figure(1, figsize=(9, 6))
plt.plot(t, x)