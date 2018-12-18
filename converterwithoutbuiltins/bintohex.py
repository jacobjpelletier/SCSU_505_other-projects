#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 21:57:14 2018

@author: jacobpelletier
"""

def lessthanfour(num):
    
        if num in ['0','00','000']:
            return('0')
        elif num in ['1', '01', '001']:
            return('1')
        elif num in ['10', '010']:
            return('2')
        elif num in ['11', '011']:
            return('3')
        elif num in ['100']:
            return('4')
        elif num in ['101']:
            return('5')
        elif num in ['110']:
            return('6')
        elif num in ['111']:
            return('7')
    
    
def equaltofour(num):
        if num == '1000':
            return('8')
        elif num == '1001':
            return('9')
        elif num == '1010':
            return('a')
        elif num == '1011':
            return('b')
        elif num == '1100':
            return('c')
        elif num == '1101':
            return('d')
        elif num == '1110':
            return('e')
        elif num == '1111':
            return('f')
            


def bin_to_hex(num):
    '''
    assumes input is a binary number
    returns the hexadecimal equivalent
    '''
    #
    num = str(num)
    
    #
    front = -1
    rear = -5

    #
    numoffours = (len(num)//4)
    
    #
    leftover = (len(num)%4)
    
    #
    newnum = ''
    
    while numoffours > 0:
        numoffours -= 1
        fourreversed = (num[front:rear:-1])
        fours = (fourreversed[::-1])
        newnum += equaltofour(fours)
        front -= 4
        rear -= 4
        
    newnum += lessthanfour((num[0:leftover]))
    return(newnum[::-1])

'''    
# test
num1 = '00000000' #0 (0)
num2 = '11111111100' # ff (255)
num3 = '01001110' # 4e (78)
num4 = '00010001' # 11 (17)
nums = [num1, num2, num3, num4]

for num in nums:
    print(bin_to_hex(num))

num3 = '0000'
print(bin_to_hex(num3))
'''