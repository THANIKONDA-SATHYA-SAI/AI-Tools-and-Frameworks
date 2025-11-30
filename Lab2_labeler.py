import os
import csv
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

IMAGE_FOLDER = "Lab2_images"
CSV_FILE = "Lab2_labels.csv"

people = ["Homer Simpson","Marge Simpson","Bart Simpson","Lisa Simpson","Maggie Simpson","Abe Simpson"]
envs = ["indoor","outdoor"]

files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png','.jpg','.jpeg'))]
index = 0

root = tk.Tk()
root.title("Simpsons Labeler")

img_label = tk.Label(root)
img_label.pack()

selected_person = tk.StringVar()
selected_env = tk.StringVar()

def show_image():
    global index
    if index >= len(files):
        messagebox.showinfo("Done","All images labeled!")
        root.quit()
        return
    path = os.path.join(IMAGE_FOLDER, files[index])
    img = Image.open(path)
    img = img.resize((500,500))
    tk_img = ImageTk.PhotoImage(img)
    img_label.config(image=tk_img)
    img_label.image = tk_img

def save_and_next():
    global index
    if selected_person.get() == "" or selected_env.get() == "":
        messagebox.showerror("Error","Choose both person & environment")
        return
    
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([files[index], selected_person.get(), selected_env.get()])
    
    selected_person.set("")
    selected_env.set("")
    index += 1
    show_image()

person_frame = tk.Frame(root)
person_frame.pack()
for p in people:
    tk.Radiobutton(person_frame, text=p, variable=selected_person, value=p).pack(side="left")

env_frame = tk.Frame(root)
env_frame.pack()
for e in envs:
    tk.Radiobutton(env_frame, text=e, variable=selected_env, value=e).pack(side="left")

tk.Button(root, text="Save & Next", command=save_and_next).pack(pady=10)

show_image()
root.mainloop()
