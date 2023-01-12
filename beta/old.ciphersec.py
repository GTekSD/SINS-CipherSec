#!/usr/bin/env python3

# Python program to check validation of password
# Module of regular expression is used with search()

import re
import mmap
import pyfiglet
import os
import random
import glob
from termcolor import colored

def main():
    # Get the directory path of the main.py file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Join the directory name to form the relative path to the logo directory
    directory = os.path.join(script_dir, 'logo')
    # Get the list of all the .txt files in the logo directory
    txt_files = glob.glob(os.path.join(directory, '*.txt'))
    # Choose a random file from the list
    chosen_file = random.choice(txt_files)
    # Open the file
    with open(chosen_file, 'r') as file:
        # Read the contents of the file
        contents = file.read()
        # Define a list of colors
        colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
        # Choose a random color
        color = random.choice(colors)
        # Print the contents of the file in the chosen color
        print(colored(contents, color))

if __name__ == '__main__':
    main()


"""
# import pyfiglet module
result = pyfiglet.figlet_format("SINS CipherSec", font = "future"  )
print(result)
"""

password = input("Enter password to check:- ")
flag = 0

# Passwords should contain three of the four character types:
while True:
	if (len(password)<=8):
		flag = -1
		break
		
	# Lowercase letters: a-z
	elif not re.search("[a-z]", password):
		flag = -1
		break
		
	# Uppercase letters: A-Z	
	elif not re.search("[A-Z]", password):
		flag = -1
		break
		
	# Numbers: 0-9
	elif not re.search("[0-9]", password):
		flag = -1
		break
		
	# Symbols: ~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/
	elif not re.search("[!@#$%^&*()_+}{\|;:,.><?/]" , password):
		flag = -1
		break
				
	elif re.search("\s" , password):
		flag = -1
		break
	else:
		with open('rockyou.txt') as file:
			contents = file.read()
		if password in contents:
			flag = -1
			
		break

if flag == -1:
	print("Not secured  Password ")
else:
	print("Secured  Password ")
