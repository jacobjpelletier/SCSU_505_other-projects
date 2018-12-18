#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:11:41 2018

@author: jacobpelletier
"""

def decdigit(dig):
    '''
    takes in a single decimal digit
    returns hexadecimal equivalent
    '''
    dig = str(dig)
    if dig == '0':
        return('0')
    elif dig == '1':
        return('1')
    elif dig == '2':
        return('2')
    elif dig == '3':
        return('3')
    elif dig == '4':
        return('4')
    elif dig == '5':
        return('5')
    elif dig == '6':
        return('6')
    elif dig == '7':
        return('7')
    elif dig == '8':
        return('8')
    elif dig == '9':
        return('9')
    elif dig == 'a':
        return('10')
    elif dig == 'b':
        return('11')
    elif dig == 'c':
        return('12')
    elif dig == 'd':
        return('13')
    elif dig == 'e':
        return('14')
    elif dig == 'f':
        return('15')




def hexrecur(num):
    '''
    '''
    #
    exponent = len(str(num)) 
    newnum = 0
    
    #
    for i in range(0, len(str(num))):
        exponent -= 1
        multiplier = (decdigit(num[i]))
        newnum += (int(multiplier)*(16**(exponent)))
        
    return(newnum)
    #return(newnum)

'''
# Test        
num = '4d'
print(hexrecur(num))
'''