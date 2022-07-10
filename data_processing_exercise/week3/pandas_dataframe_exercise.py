# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:19:08 2018

@author: Bangun
"""

import pandas as pd

music_data = [("the rolling stones","Satisfaction"),("Beatles","Let It Be"),("Guns N' Roses","Don't Cry"),("Metallica","Nothing Else Matters")]

music_table = pd.DataFrame(music_data)
music_table.index = range(1,5)
music_table.columns = ['artist', 'song_title']
print(music_table)