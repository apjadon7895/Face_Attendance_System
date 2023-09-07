# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 08:42:30 2023

@author: apjad
"""
 
list=['car', 'bike','honda', 'hero']
def loop(x):
    print(x*3)

    
def map_simple(crazy,list):
       for items in list:
            crazy(items)
map_simple(loop,list)
