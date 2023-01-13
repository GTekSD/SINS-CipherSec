# sctipt for password generator GUI mode

import tkinter as tk
from tkinter import messagebox
import os
import datetime

def generate_password():
    name = name_entry.get()
    passphrase = passphrase_entry.get()
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
    password_label.config(text=password)
    
def save_password():
    password = password_label.cget("text")
    name = name_entry.get()
    # Create a directory named "users" if it doesn't exist
    if not os.path.exists("users"):
        os.mkdir("users")
    # Create a subdirectory with the name entered by the user if it doesn't exist
    user_directory = "users/" + name
    if not os.path.exists(user_directory):
        os.mkdir(user_directory)
    # get the current date
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    # rename the old password file as old.password with date
    for file in os.listdir(user_directory):
        if file.endswith(".password"):
            os.rename(user_directory + '/' + file, user_directory + '/old.' + file + '.' + current_date)
    # save the new generated password with current date
    file = open(user_directory + "/password." + current_date + ".password", "w")
    file.write(password)
    file.close()
    messagebox.showinfo("Success", "Password saved to " + user_directory + ".")

def copy_password():
    password = password_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Success", "Password copied to clipboard.")


root = tk.Tk()
root.geometry("200x200")
root.title("Password Generator")

name_label = tk.Label(root, text="Enter Your Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

passphrase_label = tk.Label(root, text="Enter Your Passphrase:")
passphrase_label.pack()

passphrase_entry = tk.Entry(root)
passphrase_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root)
password_label.pack()

save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.pack()

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack()

root.mainloop()
