#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 17:02:49 2018

@author: jacobpelletier

the equation used to convert a number from decimal form to binary form is called
the 'base-q expansion form'

we can use the 'repeated division algorithm' to convert decimal form to binary form

Sources:
    1) 'https://www.cs.uky.edu/~jzhang/CS321/lecture1.pdf'
    2) 'https://blog.angularindepth.com/the-simple-math-behind-decimal-binary-
     conversion-algorithms-d30c967c9724'

"""

def dec_to_bin_converter(user_input):
    '''
    takes in an data type, assumes it is a valid int, and returns the binary form
    input: takes in an integer in decimal form
    output: returns that integers binary equivalent
    '''
    user_input = int(user_input)
    binary_in_reverse = []
    if user_input == 0:
        return '0'
    while user_input >= 1:
        binary_in_reverse.append(user_input%2)
        user_input = user_input//2
    return ''.join(str(num) for num in binary_in_reverse[::-1])

# debug tests
#user_input = 3
#print( dec_to_bin_converter(user_input))
