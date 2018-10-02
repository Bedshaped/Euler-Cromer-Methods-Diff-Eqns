# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:26:17 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt

# Defining function

def N(t, a, b):
    return a*np.exp(-t/b)

def derivative(a, b):
    return (-a/b)


# Parameters

d_t = 0.001
t_max = 10
tau = 2.0
n = int(t_max/d_t)

# Initial conditions

N_array = np.zeros((2, n))
N_array[:,0] = 10

# Loop our Euler method
x = np.linspace(0, t_max, n)
for t in range(n-1):
    N_array[0, t + 1] = N_array[0, t] + d_t*(derivative(N_array[0, t], tau))

    
# Calculate direct values

N_array[1] = N(x, N_array[1, 0], tau)

# Deviation of methods
    
dev = (N_array[1,:] - N_array[0,:])/N_array[1,:]

# Initialize the plot
    
plt.figure(1, figsize=(9, 6))
plt.plot(N_array[0,:], x, label=r"$Euler (\Delta t = \frac{1}{%5.2f}s)$" % d_t**-1)
plt.plot(N_array[1,:], x, label=r"$Direct$")
plt.xlabel("Time")
plt.ylabel("N")
plt.legend()

plt.figure(2, figsize=(9, 6))
plt.plot(x[1:], dev[1:], label=r"$Deviation$")
plt.yscale("log")
plt.xscale("log")
plt.xlabel("Time")
plt.ylabel(r"$\Delta N$")
plt.legend()

plt.show()
