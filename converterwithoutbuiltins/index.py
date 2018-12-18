#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 15:49:26 2018

@author: jacobpelletier
"""

import time
import dectohex as dh
import dectobin as db
import bintohex as bh
import bintodec as bd
import hextobin as hb
import hextodec as hd
import userinput as ui
import classconverter as cc


while True:
    
    print('----------------------------------------------------')
    print(cc.Converter.about())
    
    userchoice = ui.input_select()
    if userchoice == 'q':
        break
    
    usernumber = ui.input_num()
    if usernumber == 'q':
        break

    while True:
        
        if userchoice == 'dh':
            cnvrt = cc.Converter(usernumber)
            finalcheck = cnvrt.checkdec()
            if finalcheck == True:
                print('\n{} in hexadecimal form is: {} '
                      .format(usernumber, dh.dectohex(int(usernumber))))
                break
            
            else:
                print('\n\tEnter a valid decimal number.')
                time.sleep(2)
                break

        elif userchoice == 'db':
            cnvrt = cc.Converter(usernumber)
            finalcheck = cnvrt.checkdec()
            if finalcheck == True:
                print('\n{} in binary form is: {} '
                      .format(usernumber, db.dec_to_bin_converter(usernumber)))
                break     
            else:
                print('\n\tEnter a valid decimal number.')
                time.sleep(2)
                break
            
        elif userchoice == 'bh':
            cnvrt = cc.Converter(usernumber)
            finalcheck = cnvrt.checkbin()
            if finalcheck == True:
                print('\n{} in hexadecimal form is: {} '
                      .format(usernumber, bh.bin_to_hex(usernumber)))
                break     
            else:
                print('\n\tEnter a valid binary number.')
                time.sleep(2)
                break      
            
        elif userchoice == 'bd':
            cnvrt = cc.Converter(usernumber)
            finalcheck = cnvrt.checkbin()
            if finalcheck == True:
                print('\n{} in decimal form is: {} '
                      .format(usernumber, bd.bin_to_dec_converter(usernumber)))
                break     
            else:
                print('\n\tEnter a valid binary number.')
                time.sleep(2)
                break   
            
        elif userchoice == 'hb':
            cnvrt = cc.Converter(usernumber)
            finalcheck = cnvrt.checkhex()
            if finalcheck == True:
                print('\n{} in binary form is: {} '
                      .format(usernumber, hb.hextobin(str(usernumber))))
                break     
            else:
                print('\n\tEnter a valid hexadecimal number.')
                time.sleep(2)
                break 
            
        elif userchoice == 'hd':
            cnvrt = cc.Converter(usernumber)
            finalcheck = cnvrt.checkhex()
            if finalcheck == True:
                print('\n{} in decimal form is: {} '
                      .format(usernumber, hd.hexrecur(str(usernumber))))
                break     
            else:
                print('\n\tEnter a valid hexadecimal number.')
                time.sleep(2)
                break 
        