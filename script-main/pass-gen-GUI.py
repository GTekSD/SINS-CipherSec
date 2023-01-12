# Script for generating password GUI mode

import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

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
    if not os.path.exists("users"):
        os.mkdir("users")
    # Save the old password as old_password_<current_date>.txt
    date = datetime.now().strftime("%Y-%m-%d")
    old_password_file = open("users/old_password_" + date + ".txt", "w")
    old_password_file.write(password_label.cget("text"))
    old_password_file.close()
    # Save the new password as password_<current_date>.txt
    file = open("users/password_" + date + ".txt", "w")
    file.write(password)
    file.close()
    messagebox.showinfo("Success", "Password saved to users/password_" + date + ".txt")

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

"""
suppose im user1, i entered my name as user1 and i generated a password, so it will save in users directory but it should create a new directory which is user enter his name while generating password, and then in that newly created directory it will save password with current day.
suppose on next day, same user again generated password, then it should save in that directory where previous password contain, but not this time it will rename that previous password file as old, and save new generated password with current date.
"""
