# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:17:56 2019

@author: Holder
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False

    mid = len(aStr) // 2
    test = aStr[mid]

    if test == char:
        return True
    elif len(aStr) == 1:
        return False
    else:
        return isIn(char, aStr[:mid] if char < test else aStr[mid + 1:])

isIn('n', 'yawn')