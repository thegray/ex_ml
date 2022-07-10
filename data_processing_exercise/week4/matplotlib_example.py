# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:33:20 2018

@author: Bangun
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

plt.title("Stock Stat Cocacola")
plt.xlabel('Month')
plt.ylabel('Average Close Price')
plt.plot(x, y, 'r*')

plt.bar(x,y)

#pl.plot(x,y)