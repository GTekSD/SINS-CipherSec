# script for password checker CLI mode

import os
import re

def check_password(password):
    
    # check if the password is at least 8 characters long
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # check if the password contains at least one numeric character
    elif not any(i.isdigit() for i in password):
        return "Password must contain at least one numeric character."
    
    # check if the password contains at least one special character
    elif not any(i in "!@#$%^&*()_+-=[]{};:'\"\\|,.<>/?" for i in password):
        return "Password must contain at least one special character."
    
    # check if the password contains more than 2 consecutive repeating characters
    elif re.search(r"(\w)\1{2,}", password):
        return "Password can contain only 2 consecutive repeating characters."
    
    # check if the password contains at least one capital letter
    elif not any(i.isupper() for i in password):
        return "Password must contain at least one capital letter."
    
    # check if the password contains at least one small letter
    elif not any(i.islower() for i in password):
        return "Password must contain at least one small letter."
    
    # check if the password is in any of the .txt files in the directory
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'db-SecLists')
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename)) as file:
                if password in file.read():
                    return "Breached Password. The Password you entered is in the compromised database. Please use difficult another password"
    
    # if the password pass all the above conditions, then return valid
    else:
        return "Secure password."

password = input("Enter the password: ")
result = check_password(password)
print(result)

