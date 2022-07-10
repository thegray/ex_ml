# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:05:31 2018

@author: Bangun
"""

import time
import math
import numpy as np

x = 12345
t1 = time.clock()
res1 = math.sqrt(x)
t2 = time.clock()
res2 = np.sqrt(x)
t3 = time.clock()
print('running time math.sqrt : ', (t2-t1) * 10000)
print('running time np.sqrt : ', (t3-t2) * 10000)

res3 = math.log(x)
t4 = time.clock()
res4 = np.log(x)
t5 = time.clock()
print('running time math.log : ', (t4-t3) * 10000)
print('running time np.log : ', (t5-t4) * 10000)
