#!/usr/bin/env python3

import os
import random
import glob
import subprocess
from termcolor import colored

def main():

    # Get the directory path of the main.py file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Join the directory name to form the relative path to the logo directory
    directory = os.path.join(script_dir, 'logo')
    # Get the list of all the .txt files in the logo directory
    txt_files = glob.glob(os.path.join(directory, '*.txt'))
    # Choose a random file from the list
    chosen_file = random.choice(txt_files)
    # Open the file
    with open(chosen_file, 'r') as file:
        # Read the contents of the file
        contents = file.read()
        # Define a list of colors
        colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
        # Choose a random color
        color = random.choice(colors)
        # Print the contents of the file in the chosen color
        print(colored(contents, color))


    # Get the directory path of the main.py file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Join the directory name to form the relative path to the desired directory
    directory = os.path.join(script_dir, 'features')
    print("What do you want to do next?")
    print("1. Checker")
    print("2. Generator")
    choice = input("Enter your choice(1/2): ")
    if choice == "1":
        subprocess.call(["python", os.path.join(directory, "checker.py")])
    elif choice == "2":
        subprocess.call(["python", os.path.join(directory, "generator.py")])
    else:
        print("Invalid choice")

if __name__ == '__main__':
    main()

