# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 20:49:35 2019

@author: Holder
"""

x = 23
epsilon = 0.1
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
        print(guess, abs(guess**2-x), epsilon)
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))