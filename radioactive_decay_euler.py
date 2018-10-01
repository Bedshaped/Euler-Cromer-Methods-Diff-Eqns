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


# Parameters

d_t = 0.1
t_max = 10
tau = 2.0
n = int(t_max/d_t)

# Initial conditions

N_array = np.zeros((2, n))
N_array[:,0] = 10

# Loop
x = np.linspace(0, t_max, n)
for t in range(n-1):
    
    value = N(x[t], N_array[0, 0], tau) - (N(x[t], N_array[0, 0], tau)/tau)*d_t
    N_array[0, t + 1] = value

for t in range(n-1):
    value = N(x[t+1], N_array[1, 0], tau)
    N_array[1, t + 1] = value

# Deviation of methods
    
dev = np.subtract(N_array[1,:], N_array[0,:])

# Initialize the plot
    
plt.figure(1, figsize=(9, 6))
plt.plot(N_array[0,:], x, label=r"$Euler (\Delta t = \frac{1}{%5.2f}s)$" % d_t**-1)
plt.plot(N_array[1,:], x, label=r"$Direct$")
plt.xlabel("Time")
plt.ylabel("N")
plt.legend()

plt.figure(2, figsize=(9, 6))
plt.plot(x[1:], dev[1:], label=r"$Deviation$")
plt.xlabel("Time")
plt.ylabel(r"$\Delta N$")
plt.legend()

plt.show()
