# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 01:07:07 2018

@author: Bangun
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
t = pd.DataFrame(y, index = x)
t.plot()