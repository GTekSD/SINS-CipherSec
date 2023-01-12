import sys
import getpass

def generate_password():
    name = input("Enter Your Name:")
    passphrase = getpass.getpass("Enter Your Passphrase:")
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
    print("Generated Password:", password)
    save = input("Do you want to save the password in password.txt file? (y/n)")
    if save.lower() == 'y':
        try:
            with open("password.txt", "w") as f:
                f.write(password)
            print("Password saved to password.txt.")
        except:
            print("Error occured while saving password")
    copy = input("Do you want to copy the password to clipboard? (y/n)")
    if copy.lower() == 'y':
        import pyperclip
        pyperclip.copy(password)
        print("Password copied to clipboard.")
    else:
        sys.exit()

generate_password()
