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
    return password

def save_password(password):
    # Get the current date
    date = datetime.now().strftime("%Y-%m-%d")
    # Create the user directory with the name entered by the user
    user_directory = "users/" + name_entry.get()
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

password = generate_password()
save_password(password)


"""

import sys #importing sys module to exit the program
import getpass #importing getpass module to hide the entered passphrase
import pyperclip # importing pyperclip module to copy the password to clipboard

def generate_password():
    #prompting user for name
    name = input("Enter Your Name:")
    #prompting user for passphrase and hiding it
    passphrase = getpass.getpass("Enter Your Passphrase:")
    password = ""
    j = 0
    for i in range(len(passphrase)):
        char = passphrase[i]
        #looping the name if passphrase is longer
        if j == len(name):
            j = 0
        #generating password by adding ascii value of name and passphrase
        x = (ord(char) + ord(name[j])) % 26
        x += ord('A')
        password += chr(x)
        j += 1
    #printing the generated password
    print("Generated Password:", password)
    #prompting user to save the password
    save = input("Do you want to save the password in password.txt file? (y/n)")
    if save.lower() == 'y':
        try:
            with open("password.txt", "w") as f:
                f.write(password)
            print("Password saved to password.txt.")
        except:
            print("Error occured while saving password")
    #prompting user to copy the password to clipboard
    copy = input("Do you want to copy the password to clipboard? (y/n)")
    if copy.lower() == 'y':
        pyperclip.copy(password)
        print("Password copied to clipboard.")
    else:
        sys.exit()

# calling the function to execute the code
generate_password()
"""
