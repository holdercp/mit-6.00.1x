# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:49:28 2019

@author: Holder
"""
import string

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
    lcAlpha = string.ascii_lowercase
    ucAlpha = string.ascii_uppercase
    shiftedDict = {}

    def addToDict(alphaString):
        for i, char in enumerate(alphaString):
            shiftedDict[char] = alphaString[(i + shift) % 26]

    addToDict(lcAlpha)
    addToDict(ucAlpha)

    return shiftedDict

print(build_shift_dict(3))
build_shift_dict(0)
print(build_shift_dict(25))