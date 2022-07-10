# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:39:40 2018

@author: Bangun
"""

import pandas as pd

filepath = r"..\scores.xlsx"

scores = pd.read_excel(filepath)
scores.boxplot()