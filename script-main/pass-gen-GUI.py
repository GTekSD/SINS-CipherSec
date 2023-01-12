import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def generate_password():
    # Get the name and passphrase entered by the user
    name = name_entry.get()
    passphrase = passphrase_entry.get()

    password = ""
    j = 0
    # Generate the password using the name and passphrase
    for i in range(len(passphrase)):
        char = passphrase[i]
        if j == len(name):
            j = 0
        x = (ord(char) + ord(name[j])) % 26
        x += ord('A')
        password += chr(x)
        j += 1
    # Update the password label with the generated password
    password_label.config(text=password)

def save_password():
    # Get the generated password
    password = password_label.cget("text")
    # Get the current date
    date = datetime.now().strftime("%Y-%m-%d")
    # Create the user directory with the name entered by the user
    user_directory = "users/" + name_entry.get()
    # Check if the directory already exists
    if not os.path.exists(user_directory):
        os.mkdir(user_directory)
    else:
        # Rename the previous password file as old_password_<current_date>.txt
        os.rename(user_directory+"/password_"+date+".txt",user_directory+"/old_password_"+date+".txt")
    # Save the new password in the user directory with the current date
    file = open(user_directory+"/password_" + date + ".txt", "w")
    file.write(password)
    file.close()
    # Show a message box with the location of the saved password
    messagebox.showinfo("Success", "Password saved to "+user_directory+"/password_" + date + ".txt")

def copy_password():
    # Get the generated password
    password = password_label.cget("text")
    # Clear the clipboard
    root.clipboard_clear()
    # Append the password to the clipboard
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

