#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 16:41:14 2018

@author: jacobpelletier
"""


'''
Your program should:

Request the XML file name from the user
Request the desired CSV file name from the user
Read in the XML file
Convert the XML format to the CSV format
Write out the CSV file

Handle exceptions when reading and writing the files
I see two approaches to this assignment.  The first is using what you have 
learned about programming so far and build all the functionality yourself 
(this is possible with what you know).  The second is exploring Python modules 
to find the existing code to do read XML data, write CSV data, and handle data 
frames.  

'''
import time
import os
import csv
import xml.etree.ElementTree as ET

class Xml_to_Csv():
    
    def __init__(self, xmlname, csvname):
        self.xmlname = xmlname
        self.csvname = csvname
     
    def convert(self):    
        '''
        '''
        # parse xml file into data tree onto memory
        tree = ET.parse(xmlname)
        
        # defining root element with getroot() method
        root = tree.getroot()
        
        # create a new csv file
        with open(csvname, 'w', newline='') as outputfile:
            writer = csv.writer(outputfile)
            #writer.writerow(['\n\t'+root.tag])
            labels = []
            for child in root:
                for element in child:
                    if element.tag not in labels:
                        labels.append(element.tag)
            writer.writerow(labels)            
            for child in root:
                listofstuff = []
                for element in child:
                    print('\nWriting row. . .')
                    time.sleep(0.05)
                    listofstuff.append('{}'.format(element.text))
                writer.writerow(listofstuff)
        
        outputfile.close()
        return('\nFile conversion complete. Find file in '+os.getcwd())

print('\nInstructions: \nOpen this file in the same directory as where the XML'
      ' file is located. This program will then create a new CSV file'
      ' from the XML data. \n\nEnter names without their extensions.')

print('Starting Program. . .')

time.sleep(3)
directory = os.getcwd()

while True:
    
    #get name of file to PARSE from user
    xmlname = input('Enter name of XML file you would like to open: ')

    #add file extention to filename for filesystem
    xmlname = xmlname+'.xml'

    #get name of file to WRITE TO from user
    csvname = input('Enter name of CSV file you would create: ')

    #add file extention to filename for filesystem 
    csvname = csvname+'.csv'
    
    # if file in current currectory
    if os.path.exists(os.path.join(directory, xmlname)):
        break
    else:
        print('\nEnter a valid filename.')

#initialize class with user input to start writing program
newfile = Xml_to_Csv(xmlname, csvname)

#run file conversion method
print(newfile.convert())




                

    
