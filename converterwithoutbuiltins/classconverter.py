#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 14:27:55 2018

@author: jacobpelletier
"""

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
        number = str(self.number.lower())

        for num in number:
                
            if num not in (['0','1','2','3','4','5','6','7','8','9','a',
                           'b','c','d','e','f']):
   
                return('Enter a valid hexadecimal digit.')
                #exit the for loop after indicating that number is not valid
                break
            
        # otherwise return True if the all nums in list
        return True
    
    def checkdec(self):
        """
        """
        number = str(self.number)
        
        for num in number:
                
            if num not in ['0','1','2','3','4','5','6','7','8','9']:
   
                return('Enter a valid decimal digit.')
                #exit the for loop after indicating that number is not valid
            
                break
        # otherwise return True if the all nums in list               
        return True
            
    def checkbin(self):
        """
        """
        number = str(self.number)
        
        for num in number:
                
            if num not in ['0','1']:
   
                return('Enter a valid binary digit.')
                #exit the for loop after indicating that number is not valid
                
                break
        # otherwise return True if the all nums in list               
        return True
    
    @staticmethod
    def about():
        """Returns information about the program"""
        return('\n Welcome to the program. You can convert a number bewtween '
          'hexadecimal, decimal, and binary.\n\nTo convert FROM hexadecimal TO '
          'decimal, enter: \'hd\' \nTo convert FROM hexadecimal TO binary, enter: \'hb\' '
          '\nTo convert FROM decimal TO hexadecimal, enter: \'dh\' \nTo convert FROM '
          'decimal TO binary, enter: \'db\' \nTo convert FROM binary TO hexadecimal '
          ',enter: \'bh\' \nTo convert FROM binary TO decimal, enter: \'bd\''
          '\n\nEnter \'q\' to quit program at any time.')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        