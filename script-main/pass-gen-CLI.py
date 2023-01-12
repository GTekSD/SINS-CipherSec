# Script for generating password CLI mode

import os
from datetime import datetime

def generate_password():
    # Get the name and passphrase entered by the user
    name = input("Enter Your Name: ")
    passphrase = input("Enter Your Passphrase: ")

    password = ""
    j = 0
    # Generate the password using the name and passphrase
    for i in range(len(passphrase)):
        char = passphrase[i]
        if j == len(name):
            j = 0
        x = (ord(char) + ord(name[j])) % 26
        x += ord('A')
        password += chr(x)
        j += 1
    # Print the generated password
    print(password)
    return password,name

def save_password(password,name):
    # Get the current date
    date = datetime.now().strftime("%Y-%m-%d")
    # Create the user directory with the name entered by the user
    user_directory = "users/" + name
    # Check if the directory already exists
    if not os.path.exists(user_directory):
        os.mkdir(user_directory)
    else:
        # Rename the previous password file as old_password_<current_date>.txt
        os.rename(user_directory+"/password_"+date+".txt",user_directory+"/old_password_"+date+".txt")
    # Save the new password in the user directory with the current date
    file = open(user_directory+"/password_" + date + ".txt", "w")
    file.write(password)
    file.close()
    # Show a message with the location of the saved password
    print("Password saved to "+user_directory+"/password_" + date + ".txt")

password,name = generate_password()
save_password(password,name)

