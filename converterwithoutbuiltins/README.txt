Converter program README
November, 4, 2018.
Jacob Pelletier

CSC 505 - Computer Programming and Data Structures. 

Assignment 5C- Number Converting System:

"Write a single program that converts numbers between the different numbering systems we discussed in class.  The program should be able to convert:

binary to decimal,
decimal to binary,
hexadecimal to decimal,
decimal to hexadecimal,
binary to hexadecimal,
and hexadecimal to binary.
Submit the assignment on GitHub"
___________________________

Purpose:    The purpose of this program is to convert a number between hexadecimal, 
	    decimal, and binary. All required files are located within the directory 
	    "converterwithoutbuiltins".

Directions: To use the program, run index.py from the directory.

About: The directory contains the following files:
	1) index.py: 
		a) main logic of the program that imports all other files
	2) classconcerter.py:
		a) this file is to be used on a user given number. Upon initialization, 
		   methods can be accessed which allow:
			- describe the program and instructions which guide 
			  userinput.input_select()
			- checking of 1) hex, 2) binary, 3) decimal, number groups before 
		          final pass to conversion
	3) userinput.py:
		a) this file is to be used to gather user input. This file includes 
	           two functions:
			-input_num() which is used to pass to the program what number the 
			 user would like to convert.
				- this file does a first-pass filter to ensure input is a 
				  valid hex/dec/bin number
				- allows for user to input "quit" input
			-input_select() which is used to pass to the program the conversion 
			 which the user would like to perform
				- this file filters for valid inputs.
				- allows for user to input "quit" input
	4) dectohex.py:
		a) takes in a valid decimal and returns the equivalent hexadecimal
	5) dectobin.py:
		a) takes in a valid decimal and returns the equivalent binary
	6) bintohex.py:
		a) takes in a valid binary and returns the equivalent hexadecimal
	7) bintodec.py:
		a) takes in a valid binary and returns the equivalent decimal
	8) hextodec.py:
		a) takes in a valid hexadecimal and returns the equivalent decimal
	9) hextobin.py
		a) takes in a valid hexadecimal and returns the equivalent binary
