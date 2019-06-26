# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = 'azcbobobegghakl'
substr1 = ""
substr2 = ""

for i, char in enumerate(s, 1):
    substr1 += char

    if i == len(s):
        break

    if char > s[i]:
        if len(substr2) < len(substr1):
            substr2 = substr1

        substr1 = ""


print("Longest substring in alphabetical order is: " + substr1 if len(substr1) > len(substr2) else substr2)
