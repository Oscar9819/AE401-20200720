# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:31:16 2020

@author: user
"""
import random

abc =random.randint(1,1)

n =input('猜一個數字:')
n =int(n)

if abc == n:
    print('猜對了')
    
else:
   print('猜錯了!答案是', abc)
