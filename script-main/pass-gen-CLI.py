# Script for generating password CLI mode

import os
import datetime

# function to generate password
def generate_password():
    name = input("Enter Your Name: ")
    passphrase = input("Enter Your Passphrase: ")
    password = ""
    j = 0
    for i in range(len(passphrase)):
        char = passphrase[i]
        if j == len(name):
            j = 0
        x = (ord(char) + ord(name[j])) % 26
        x += ord('A')
        password += chr(x)
        j += 1
    print("Generated Password: ", password)
    return password,name

# function to save password
def save_password(password,name):
    #get the current date
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    # create the directory "users" if it does not exist
    if not os.path.exists("users"):
        os.makedirs("users")
    # create a directory with the user's name if it does not exist
    user_directory = "users/" + name
    if not os.path.exists(user_directory):
        os.makedirs(user_directory)
    # rename the previous password file to "old.password" if it exists
    if os.path.exists(user_directory+'/password.txt'):
        os.rename(user_directory+'/password.txt', user_directory+'/old.password')
    # save the new password to a file with the current date as the file name
    file = open(user_directory + "/password"+current_date+".txt", "w")
    file.write(password)
    file.close()
    print("Password saved to "+user_directory+"/password"+current_date+".txt.")

# main function to call other functions
def main():
    password,name = generate_password()
    save_password(password,name)

# call the main function
if __name__ == '__main__':
    main()
