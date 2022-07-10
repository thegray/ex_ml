# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:42:31 2018

@author: Bangun
"""

dict_mark_1 = {'Wang': 98, 'Li': 87, 'Ma': 93}
dict_mark_2 = {'Li': 90, 'Ma': 95, 'Xu': 75}
dict_mark_1.update(dict_mark_2)
dict_mark_1.pop('Li')

########

color = {"color":[
    	           {"warm":["red","orange","yellow"]},
                 {"cold":["cyan","blue"]},
                 {"neutral":["purple","green","black","gray","white"]}
                 ]
        }

print(color['color'][1]['cold'])
res = color['color']['cold'][1]

#########

import numpy as np
a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
a[[2]].sum()

##########

from pandas import Series
sa = Series(['a', 'b', 'c'], index = [0, 1, 2])
sb = Series(['a', 'b', 'c'])
sc = Series(['a', 'c', 'b'])
sa.equals(sc)
sb.equals(sa)

############
from pandas import DataFrame
data = {'language': ['Java', 'PHP', 'Python', 'R', 'C#'],
            'year': [ 1995 ,  1995 , 1991   ,1993, 2000]}
frame = DataFrame(data)
frame['IDE'] = Series(['Intellij', 'Notepad', 'IPython', 'R studio', 'VS'])
'VS' in frame['IDE']
frame['year'][2]
frame['Tes'] = [11,22,33,44,55]

##############

def find_person(dict_users, strU):
      if dict_users.get(strU):
          return dict_users[strU]
      else:
          return 'Not Found'

dict_users = {'Tom':88888,'Jerry':5555555,'Snoopy':11111,'Pooh':12341234,'Luffy':1212121}
strU =  input('Please input the name: ')
print(find_person(dict_users, strU))





