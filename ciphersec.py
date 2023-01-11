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
password = input("Enter password:- ")
flag = 0
while True:
	if (len(password)<=8):
		flag = -1
		break
	elif not re.search("[a-z]", password):
		flag = -1
		break
	elif not re.search("[A-Z]", password):
		flag = -1
		break
	elif not re.search("[0-9]", password):
		flag = -1
		break
	elif not re.search("[_@$]" , password):
		flag = -1
		break
	elif re.search("\s" , password):
		flag = -1
		break
	else:
		flag = 0
		print("Valid Password")
		with open(r'/home/manoj/Desktop/rockyou.txt', 'rb', 0) as file:
                     s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
                     if s.find(b'password') != -1:
                        print('compromised')
                  
                     else:
                        print('valid')

		break

if flag == -1:
	print("secured  Password ")

