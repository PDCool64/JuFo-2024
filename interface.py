import glob
import tkinter as tk
from turtle import window_width
import numpy as np
import os
from PIL import ImageTk, Image

def process(path, yellow_threshold, counter_threshold, image_label, original_picture):
    global image_thing
    global image_thing_original
    im = Image.open(path)
    image_thing_original = ImageTk.PhotoImage(im)
    original_picture.config(image=image_thing_original)
    image_array = np.array(im)
    height, width, colors = image_array.shape
    res = np.zeros((height, width), dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            yellow = 255 - image_array[y, x, 0] + 255 - image_array[y, x, 1] + image_array[y, x, 2]
            yellow = 255 - yellow if yellow < 255 else 0
            res[y, x] = yellow
    image_thing = ImageTk.PhotoImage(Image.fromarray(res))
    image_label.config(image=image_thing)


window = tk.Tk()
window.title('Jugend Forscht')
window.geometry('800x500')
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=0)
window.rowconfigure(2, weight=0)
window.rowconfigure(3, weight=3)


# Inputs
yellow_threshold = tk.Entry(window)
yellow_threshold.grid(row=0, column=1)
counter_threshold = tk.Entry(window)
counter_threshold.grid(row=1, column=1)
image_chooser = tk.Entry(window)
image_chooser.grid(row=2, column=1)

# Buttons


image_thing = ImageTk.PhotoImage(Image.open("Test_Images/test1.jpg"))
image_thing_original = ImageTk.PhotoImage(Image.open("Test_Images/test1.jpg"))
im = Image.open("Test_Images/test1.jpg")
image = ImageTk.PhotoImage(im)
original_picture = tk.Label(window, image=image)
original_picture.grid(row=0, column=2, rowspan=2)
label = tk.Label(window, image=image)
label.grid(row=2, column=2, rowspan=2)

apply_button = tk.Button(window, text="Process", command=lambda : process(f"Test_Images/test{image_chooser.get()}.jpg", yellow_threshold.get(), counter_threshold.get(), label, original_picture))
apply_button.grid(row=3, column=0, columnspan=2)

window.mainloop()