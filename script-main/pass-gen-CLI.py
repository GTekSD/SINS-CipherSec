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
