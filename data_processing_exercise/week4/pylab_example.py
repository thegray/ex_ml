# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 00:55:44 2018

@author: Bangun
"""

import pylab as pl
import numpy as np

pl.figure(figsize=(8,6),dpi=100)

t = np.arange(0.,4.,0.1)

pl.plot(t,t,color='red',linestyle='-',linewidth=3,label='Line 1')
pl.plot(t,t+2,color='green',linestyle='',marker='*',linewidth=3,label='Line 2')
pl.plot(t,t**2,color='blue',linestyle='',marker='+',linewidth=3,label='Line 3')

pl.legend(loc='upper left')