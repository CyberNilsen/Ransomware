import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Ransomware")
root.configure(bg="black")
#import tkinter and pillow, creates the program, sets background color and sets the title.

root.overrideredirect(True)
root.protocol("WM_DELETE_WINDOW", lambda: None)
#Removes the menu bar and also dosent allow the window to be closed.

image_path = "Skull.png"
#Says where the path to the picture is.

original_image = Image.open(image_path)
#Makes a variable with the picture.

resized_image = original_image.resize((700, 400)) 
#Resizes the picture size.

image = ImageTk.PhotoImage(resized_image)
#Makes a variable that tk can use.

image_label = tk.Label(root, image=image, bg="black")
image_label.place(relx=0.5, rely=0.4, anchor="center")
#Sets picture in center and makes background black.

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#Fetches the actual size of your main monitor. Width and height.



root.geometry(f"{screen_width}x{screen_height}+{0}+{0}")
#Creates the window and sets the width and height that is defined and also the position.

root.mainloop()
#Starts the actual program.
