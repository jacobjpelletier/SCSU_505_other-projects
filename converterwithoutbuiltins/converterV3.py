#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 14:27:55 2018

@author: jacobpelletier
"""

import dectohex as dh
import dectobin as db
import bintohex as bh
import bintodec as bd
import hextobin as hb
import hextodec as hd

print('\n Welcome to the program. You can convert a number bewtween '
      'hexadecimal, decimal, and binary.\n\nTo convert FROM hexadecimal TO '
      'decimal, enter: \'hd\' \nTo convert FROM hexadecimal TO binary, enter: \'hb\' '
      '\nTo convert FROM decimal TO hexadecimal, enter: \'dh\' \nTo convert FROM '
      'decimal TO binary, enter: \'db\' \nTo convert FROM binary TO hexadecimal '
      ',enter: \'bh\' \nTo convert FROM binary TO decimal, enter: \'bd\'')

class Converter(object):
    """
    """
    
    def __init__(self, number):
        """initialize with number attribute"""
        self.number = number
        
    def getnumber(self):
        """Returns number attribute"""
        return(self.number)
        
    def checkhex(self):
        """
        """
        number = self.number.lower()
        correct = True
        
        while True:
            
            for num in number:
                
                if num in (['0','1','2','3','4','5','6','7','8','9','a','b','c'
                           ,'d','e','f']):
   
                else:
                    print('Enter a valid hexadecimal digit.')
            
            

        