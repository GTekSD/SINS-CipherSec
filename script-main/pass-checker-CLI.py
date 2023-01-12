import re

# function to check the password
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
    # check if the password contains any consecutive repeating characters
    elif re.search(r"(\w)\1", password):
        return "Password cannot contain any consecutive repeating characters."
    # if the password pass all the above conditions, then return valid
    else:
        return "Password is valid."

password = input("Enter the password: ")
result = check_password(password)
print(result)
