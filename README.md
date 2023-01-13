
<h1 align="center">
  <br>
    <a href="https://github.com/GTekSD/SINS-CipherSec.git"><img src="static/sins-main2-logo.jpg" alt="CipherSec"></a>
  </br>
</h1>


# SINS-CipherSec

![Build](https://img.shields.io/badge/Built%20with-Python-Blue)
![License](https://img.shields.io/badge/license-GNU_General_Public_License-_red.svg)

> "Advanced Password Management with SINS CipherSec: Securing Online Accounts with Unbreakable Passwords"

A python script to help people secure their online accounts by generating strong, unique passwords and storing them in a secure manner and help people assess the strength of their passwords and generate new, stronger passwords if necessary. This could involve creating a simple password checker.

*SINS-CipherSec** is being actively developed by [@GTekSD](https://twitter.com/GTekSD) [@Pathamadia](https://twitter.com/) [@SanoJ](https://twitter.com/) and [@K4D4F](https://twitter.com/)

# Installation

**Requirement: python 3 or higher**

Choose one of these installation options:

- Install with **git**: `git clone https://github.com/GTekSD/SINS-CipherSec.git`
- Install **Requirements** `pip3 install -r requirements.txt`

**To run your script by typing just the script name, you need to make it executable and also need to specify the interpreter to use using shabang line.**

- Add the shebang line at the top of your ciphersec.py file: `#!/usr/bin/env python`.
- Make the script executable by running the following command `chmod +x ciphersec.py`
- Add the path of your script to the system's PATH environment variable.
- Now you should be able to run your script by typing just the script name in terminal.

There are several ways to add a directory to the system's PATH environment variable. Here are a few common methods:

- You can add the directory to the PATH in the shell startup file, such as .bashrc or .bash_profile for bash shell, or .zshrc for zsh shell. You can open the file in a text editor and add the line `export PATH=$PATH:/path/to/directory` (replace /path/to/directory with the actual path to the directory containing your script)

- You can also add the path of your script in the terminal, by running the command `export PATH=$PATH:/path/to/SINS-CipherSec` (replace /path/to/SINS-CipherSec with the actual path to the directory containing your script)

- If you want to add the path permanently, you can also add the path to the /etc/environment file. This will make the path available to all users and will persist after reboot.
- or hit cmd `source .zshrc` for kali linux
- Manually add path in .zshrsc file
Example: 
```
# SINS CipherSec
alias ciphersec='python3 /home/kali/Tools/SINS-CipherSec/ciphersec.py'
export PATH=$PATH:/home/kali/Tools/SINS-CipherSec
```

Please note that the method to add path may vary depending on the Operating system you are using.


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


