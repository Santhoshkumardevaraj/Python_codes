# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 00:54:06 2021

@author: Defender
"""

def add_it_up(num):
    try:
        num=int(num)
    except ValueError:
        print(num,' is not a integer')
    else:
        i=0
        while num>0:
            i=i+num
            num=num-1
        print('SUM= ',i)
    
add_it_up(1000);