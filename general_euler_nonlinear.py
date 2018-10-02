# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:54:54 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt

# Defining function

def dxdt(a, b):
    return b - a**2

# Parameters

h = 0.05
t_max = 9
n = int(t_max/h)

# Initial conditions

initial_vals = [3, 1, 0, -0.72, -0.73, -5]
x = np.zeros((len(initial_vals),n))
t = np.linspace(0, t_max, n)

# Loop and initialize our initial values

k = 0
for j in initial_vals:
    x[k, 0] = j
    w = k
    k += 1
    for i in range(n-1):
        x[w, i + 1] = x[w, i] + h*dxdt(x[w, i], t[i])
        


# Initialize the plot

plt.figure(1, figsize=(9, 6))
for i in range(k):  
    plt.plot(t, x[i,], label=r"$x_0 = %5.2f$" % x[i,0])
plt.xlabel("Time")
plt.ylabel("X")
plt.legend()
axes = plt.gca()
axes.set_xlim([0,t_max])
axes.set_ylim([-5,5])