#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:27:26 2018

@author: jacobpelletier
"""



def hextobin(num):
    '''
    assumes input is a hexadecimal number
    returns its binary equivalent
    '''
    newnum = ''
    
    for char in num:
        
        if char == 'a':
            newnum += '1010'
        elif char == 'b':
            newnum += '1011'
        elif char == 'c':
            newnum += '1100'
        elif char == 'd':
            newnum += '1101'
        elif char  == 'e':
            newnum += '1110'
        elif char == 'f':
            newnum += '1111'
        elif char == '0':
            newnum += '0000'
        elif char == '1':
            newnum += '0001'
        elif char == '2':
            newnum += '0010'
        elif char == '3':
            newnum += '0011'
        elif char == '4':
            newnum += '0100'
        elif char == '5':
            newnum += '0101'
        elif char == '6':
            newnum += '0110'
        elif char == '7':
            newnum += '0111'
        elif char == '8':
            newnum += '1000'
        elif char == '9':
            newnum += '1001'
    if newnum == '0000':
        return(newnum)
    else:        
        return(newnum.lstrip('0'))
    
'''
# TEST
num = 80
print(hextobin(str(num)))
'''