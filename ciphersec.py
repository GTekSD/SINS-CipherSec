import re
import pyfiglet

# import pyfiglet module
result = pyfiglet.figlet_format("SINS CipherSec", font = "future"  )
print(result)

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
