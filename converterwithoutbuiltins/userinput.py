#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 15:56:28 2018

@author: jacobpelletier
"""

def input_num():
    '''
    returns a string of a valid int for hex/dec/bin converter
    '''
    
    while True:
        user_decimal = input('Enter a number to convert: ')
        
        try:
            for char in user_decimal:
                if char in (['1','2','3','4','5','6','7','8','9','0', 'a',
                            'b','c','d','e','f','q']):    
                    return (user_decimal)
                    break
        except:
            print('Enter a valid integer.')

def input_select():
    '''
    returns a valid selection for hex/dec/bin converter    
    '''
    
    while True:
        
        whichconvert = input('\nEnter choice here: ')
        
        try:
            if whichconvert in ['hd','hb','dh','db','bh','bd','q']:
                return(whichconvert)
                break
        
        except:
            print('\nOops. Enter a valid choice.')