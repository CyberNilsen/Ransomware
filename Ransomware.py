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