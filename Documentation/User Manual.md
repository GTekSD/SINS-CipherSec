User Manual
------------

# Introduction:
The SINS CipherSec tool is designed to help users secure their online accounts by generating strong, unique passwords and storing them in a secure manner. The tool also includes a password strength checker to help users assess the strength of their current passwords and generate new, stronger passwords if necessary.

# Getting Started:
To use the SINS CipherSec tool, first make sure you have Python 3 installed on your system. Then, download the SINS CipherSec package from the GitHub repository.

# Installation:
The SINS CipherSec tool can be installed using the following steps:

- Open a terminal window and navigate to the directory where you have downloaded the SINS CipherSec package.
- Run the command "pip install -r requirements.txt" to install the necessary dependencies.
- Run the command "python ciphersec.py" to start the tool.

# Using the CLI Interface:
The SINS CipherSec tool can be used in CLI (Command Line Interface) mode by running the command "python ciphersec.py -c" in the terminal. In CLI mode, the tool will prompt the user for their name and passphrase, and will then generate and display a password. The user can also choose to save the generated password by entering "y" when prompted.

# Using the GUI Interface:
The SINS CipherSec tool can also be used in GUI (Graphical User Interface) mode by running the command "python ciphersec.py -g" in the terminal. In GUI mode, the user will be presented with a graphical interface where they can enter their name and passphrase, and generate and view their password. The user can also save their generated password and copy it to their clipboard.

# Password Strength Checker:
The SINS CipherSec tool includes a password strength checker that can be accessed by running the command "python pass-checker-CLI.py" or "python pass-checker-GUI.py" in the terminal. In the password strength checker, the user can enter their current password and the tool will give them a score based on the strength of their password.

# Password Saving and Tracking:
The SINS CipherSec tool allows users to save their generated passwords for future reference. Passwords are saved in a directory named "users" in the format "password.yyyy-mm-dd.password" where "yyyy-mm-dd" is the current date. The tool also keeps track of previous passwords by renaming them as "old.password.yyyy-mm-dd".

# Conclusion:
The SINS CipherSec tool is a useful tool for securing online accounts by generating strong, unique passwords and storing them in a secure manner. The tool also includes a password strength checker to help users assess the strength of their current passwords and generate new, stronger passwords if necessary.
