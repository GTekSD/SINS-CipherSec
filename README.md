<h1 align="center">
  <img src="static/sins-main-logo.png" alt="CipherSec" width="200px">
  <br>
</h1>

# SINS-CipherSec
A python script to help people secure their online accounts by generating strong, unique passwords and storing them in a secure manner and help people assess the strength of their passwords and generate new, stronger passwords if necessary. This could involve creating a simple password checker.

# Manual
- For the python script, which helps people secure their online accounts by generating strong, unique passwords and storing them in a secure manner:

- Make sure you have the necessary libraries installed: string, random, base64, and cryptography. You can install these libraries using pip install.

- The script has four main functions: generate_password, encrypt_password, decrypt_password, and store_password.

- generate_password generates a strong, unique password of a specified length (16 characters by default). It uses a combination of letters, numbers, and special characters to create the password.

- encrypt_password and decrypt_password use the Fernet module from the cryptography library to encrypt and decrypt passwords, respectively. They take a password and a key as arguments, and return the encrypted or decrypted password.

- store_password stores a password for a specific website and username. It takes the website, username, password, and key as arguments, and stores the encrypted password in a file or a database.

- retrieve_password retrieves a password for a specific website and username. It takes the website, username, and key as arguments, and returns the decrypted password.

- check_password_strength checks the strength of a password. It returns a message indicating whether the password is strong or weak, and provides guidance on how to improve a weak password.

- The script generates a key to encrypt and decrypt passwords using the Fernet.generate_key function. It then uses this key to store and retrieve passwords for a specific website.

- You can use the script by calling the relevant functions and passing the necessary arguments. For example, to generate and store a new password for a website, you can call generate_password, store_password, and retrieve_password with the appropriate arguments.
