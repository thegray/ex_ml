# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:59:09 2018

@author: Bangun
"""

import nltk
from nltk.corpus import brown

#nltk.download()

cfd = nltk.ConditionalFreqDist((genre, word)
           for genre in brown.categories()
           for word in brown.words(categories = genre))
genres = ['news', 'romance']
modals = ['can', 'could', 'may', 'might', 'must', 'will', 'would']
cfd.tabulate(conditions = genres, samples = modals)
cfd.plot(conditions = genres, samples = modals)