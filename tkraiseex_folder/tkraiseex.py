import tkinter as tk
from PIL import Image, ImageTk
import random 

root = tk.Tk()
root.geometry("700x500")

val_frame = tk.Frame(root)
plu_frame = tk.Frame(root)
gar_frame = tk.Frame(root)
dah_frame = tk.Frame(root)

def add_images(): 
    dict = {val_frame: "valencia.jpg", 
            plu_frame: "plumeria.jpg",
            gar_frame: "garden.jpeg",
            dah_frame: "dahlia.jpg"}
    
    for frame, file in dict.items():
        pil_image = Image.open(fr"tkinter stuff\tkraiseex_folder\{file}")
        resized = pil_image.resize((700,500))
        tk_image = ImageTk.PhotoImage(resized)
        label = tk.Label(frame, image=tk_image)
        label.image = tk_image
        frame.grid(row=0, column=0, sticky="nsew")
        label.pack()

def change_frame():
    frame_list = [val_frame, plu_frame, gar_frame, dah_frame]
    choice = random.choice(frame_list)
    choice.tkraise()

add_images()
root.bind_all("<Key-Return>", lambda e: change_frame())

root.mainloop()