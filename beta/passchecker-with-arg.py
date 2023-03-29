import os
import re
import argparse

def check_password(password, password_list):
    
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
    
    # check if the password is in any of the password lists
    if password_list:
        with open(password_list) as file:
            if password in file.read():
                return "Breached Password. The Password you entered is in the compromised database. Please use a different password."
    
    # if the password pass all the above conditions, then return valid
    else:
        return "Secure password."


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Password Checker')
    parser.add_argument('-p', '--password', help='Password to check', required=True)
    parser.add_argument('-l', '--list', help='Password list file to check', default=None)

    args = parser.parse_args()

    result = check_password(args.password, args.list)
    print(result)
