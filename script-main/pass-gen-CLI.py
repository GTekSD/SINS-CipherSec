# Script for generating password CLI mode | v25/3/2023

import string
import random
import hashlib
import pyperclip

# function to generate password
def generate_password():
    # get user input
    username = input("Enter your username: ")
    platform = input("Enter the platform name: ")
    pin = input("Enter your PIN: ")

    # generate hash value from input values
    input_str = f"{username}{platform}{pin}"
    hash_obj = hashlib.sha256(input_str.encode())
    hash_value = int.from_bytes(hash_obj.digest(), byteorder='big')

    # use hash value to seed random number generator
    random.seed(hash_value)

    # define character sets to use for generating password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{};':\"\\|,.<>/?"

    # exclude ambiguous characters
    ambiguous_chars = "B8G6I1l0OQDS5Z2"
    for char in ambiguous_chars:
        uppercase_letters = uppercase_letters.replace(char, "")
        lowercase_letters = lowercase_letters.replace(char.lower(), "")
        digits = digits.replace(char, "")
        symbols = symbols.replace(char, "")

    # combine character sets
    char_set = uppercase_letters + lowercase_letters + digits + symbols

    # generate password
    password = ""
    while len(password) < 24:
        password += random.choice(char_set)

    # copy password to clipboard
    pyperclip.copy(password)

    # print generated password
    print("Generated Password: ", password)
    return password

# main function to call other functions
def main():
    password = generate_password()

# call the main function
if __name__ == '__main__':
    main()
