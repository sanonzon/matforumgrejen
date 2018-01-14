#!/usr/bin/env python
# -*- coding: utf-8 -*-

# qWE AS1D zxc = Qwe As1d Zxc
# osv
def normalizeTitle(input):               
    if ' ' in input:
        result = ""
        first = True
        for word in input.split():
            if first:
                result += normalizeWord(word)
            else:
                result += " " + normalizeWord(word)
        return result
    else:
        return normalizeWord(input)

def normalizeWord(word):
    first = True
    result = ""
    for char in word:
        if first and not char.isdigit():
            first = False
            result += char.upper()
        else:
            if char.isdigit():
                result += char
            else:
                result += char.lower()
    return result
