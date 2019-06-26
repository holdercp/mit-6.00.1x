# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = "azcbobobegghakl"
vowels = "aeiou"
vowelSum = 0

for vowel in vowels:
    vowelSum += s.count(vowel)
    
print(vowelSum)     