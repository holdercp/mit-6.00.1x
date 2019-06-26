# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = "azcbobobegghakl"
occurences = 0

for i, val in enumerate(s):
    if s.startswith('bob', i):
        occurences += 1

print(occurences)    
    