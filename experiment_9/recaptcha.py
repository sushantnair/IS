import os
import tkinter as tk
from PIL import Image, ImageTk
import random

selected_images_list = list()
def verify():
    river_images_list = ["r1.png", "r2.png", "r3.png"]
    # print(river_images_list)
    # print(selected_images_list)
    if river_images_list == sorted(selected_images_list):
        print('reCAPTCHA Authorization Successful')
    else:
        print('reCAPTCHA Authorization Unsuccessful')

def on_image_click(image_path):
    global selected_image
    global selected_images
    selected_image = image_path
    print(f'Selected Image: {image_path[20:]}')
    selected_images_list.append(image_path[20:])
    if len(selected_images_list) == 3:
        verify()
    elif len(selected_images_list) < 3:
        print()
        # Accept more images
    else:
        print('Too many images selected. Select each river image only once and do not select mountain image.')
        print('reCAPTCHA Authorization Unsuccessful')
    
    if image_path in selected_images:
        selected_images.remove(image_path)
    else:
        selected_images.append(image_path)
    update_image_borders()

def update_image_borders():
    for label in image_labels:
        if label.image_path in selected_images:
            label.config(borderwidth=3, relief='solid')
        else:
            label.config(borderwidth=0, relief='flat')

def create_image_grid(folder_path):
    global image_labels
    images = list()
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            # Resize the image to fit in grid box
            image.thumbnail((300, 300))
            images.append((image, image_path))
    random.shuffle(images)

    root = tk.Tk()
    root.title("Choose the Images Which Depict a River")
    for i, (image, image_path) in enumerate(images):
        row, col = divmod(i, 3)
        img = ImageTk.PhotoImage(image)
        panel = tk.Label(root, image=img)
        # Keep a reference to avoid garbage collection
        panel.image = img
        panel.grid(row=row, column=col)
        panel.bind("<Button-1>", lambda e, path=image_path: on_image_click(path))
    root.mainloop()

selected_image = None
create_image_grid("D:/Images_reCAPTCHA")