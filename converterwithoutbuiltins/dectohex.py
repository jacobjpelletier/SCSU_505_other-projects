#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:45:10 2018

@author: jacobpelletier
"""


def hexdigit(dig):
    '''
    takes in a single decimal digit
    returns hexadecimal equivalent
    '''
    if dig == 1:
        return('1')
    elif dig == 2:
        return('2')
    elif dig == 3:
        return('3')
    elif dig == 4:
        return('4')
    elif dig == 5:
        return('5')
    elif dig == 6:
        return('6')
    elif dig == 7:
        return('7')
    elif dig == 8:
        return('8')
    elif dig == 9:
        return('9')
    elif dig == 10:
        return('a')
    elif dig == 11:
        return('b')
    elif dig == 12:
        return('c')
    elif dig == 13:
        return('d')
    elif dig == 14:
        return('e')
    elif dig == 15:
        return('f')




def dectohex(num):
    '''
    takes in a multidigit decimal int
    returns hexadecimal equivalent
    '''
    
    #
    quotient = num//16
    remainder = num%16
    
    #
    newdig = ''
    
    # 
    if num == 0:
        return(0)
    else:
        newdig += hexdigit(remainder)

    #
    while quotient > 0:
        
        num = quotient 
        quotient = num//16
        remainder = num%16
        
        newdig += hexdigit(remainder)
        
    return(newdig[::-1])

# TEST 
'''
numbers = [0, 10, 20, 99, 7652]
for num in numbers:
    print(dectohex(num))
'''