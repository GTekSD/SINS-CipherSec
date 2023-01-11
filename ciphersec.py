"""length = lower = upper = digit = False

password = input('Enter the password: ')

if len(password)>= 8:
    length = True
    
    for letter in password:
        if letter.islower():
            lower = True
        elif letter.isupper():
            upper = True
        elif letter.isdigit():
            digit = True


if length and lower and upper and digit:
    print('That is a valid password.')
else:
    print('That password is not valid.')
"""

# Python program to check validation of password
# Module of regular expression is used with search()
import re
import mmap
import pyfiglet
import os
import random
import glob

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
        # Print the contents of the file
        print(contents)

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
		print('Weak Password, Password should be min 8 char long.')
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
	elif not re.search("~`!@#$%^&*()_-+={[}]|\:;'\"<,>.?/" , password):
		flag = -1
		break
		
	elif re.search("\s" , password):
		flag = -1
		break
	else:
		flag = 0
		print("Valid Password")
		with open(r'/usr/share/wordlists/rockyou.txt', 'rb', 0) as file:
                     s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
                     if s.find(b'password') != -1:
                        print('compromised')
                  
                     else:
                        print('valid')

		break

if flag == -1:
	print("secured  Password ")

