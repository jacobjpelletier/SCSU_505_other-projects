#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 17:00:08 2018

@author: jacobpelletier
"""
def bin_to_dec_converter(user_input):
    '''
    takes in an data type, assumes it is a valid int, and returns the decimal form
    input: takes in an integer in binary form
    output: returns that integers decimal equivalent
    '''
    user_input = str(user_input)
    reverse_user_input = user_input[::-1]
    decimal = 0
    for char in range(len(reverse_user_input)):
        exponent = int(char)
        if (reverse_user_input[char]) == '1':
            decimal += 2**exponent
    return(str(decimal))

#debug tests
#user_input = int('0001')
#print(bin_to_dec_converter(user_input))