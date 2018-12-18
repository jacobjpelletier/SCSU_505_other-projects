#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 22:58:05 2018

@author: jacobpelletier
"""

def palindromeformatter(palindrome):
    '''
    takes in a list or string to test
    turns list or string into a string containing lowercase alnums
    filters string and keeps only alnums. no whitespace
    returns the filtered object
    '''
    palindrome = ''.join(palindrome).lower()
    filteredpal = ''
    for item in palindrome:
        if item in 'abcdefghijklmnopqrstuvwxyz123456789':
            filteredpal+=item
    return(filteredpal)       
    


def palindromechecker(palindrome):
    '''
    assumes incoming palindrome is filtered palindrome, eg contains only alnums
    returns Boolean value revealing whether filtered palindrome is a palindrome
    '''
    if len(palindrome) <= 1:
        return True
    else: 
        return(palindrome[0] == palindrome[-1] and 
               palindromechecker(palindrome[1:-1]))
        
'''
# debug and test function    
def testpalindrome():
    
    palindrome1 = 'abc' # False
    palindrome2 = ['a','b','c','d'] # False
    palindrome3 = 'a00a' # True
    palindrome4 = ['a','1','1','a'] # True
    palindrome5 = 'abc ! cba' # True
    palindrome6 = ['a','b',' ','!', '1'] # False
    palindrome_list = [palindrome1, palindrome2, palindrome3, palindrome4,
                       palindrome5, palindrome6]
    for pal in palindrome_list:
        palindrome = palindromeformatter(pal)
        print(palindromechecker(palindrome))
    return('\nend test')

print(testpalindrome())
'''