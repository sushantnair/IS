import os
import tkinter as tk
from PIL import Image, ImageTk
import random

def on_image_click(image_path):
    global selected_images
    if image_path in selected_images:
        selected_images.remove(image_path)
    else:
        selected_images.append(image_path)
    update_image_borders()

def update_image_borders():
    for image_label in images:
        if image_label.image_path in selected_images:
            image_label.config(borderwidth=3, relief='solid')
        else:
            image_label.config(borderwidth=0, relief='flat')

def create_image_grid(folder_path):
    global images
    images = list()
    image_paths = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith(".png")]
    random.shuffle(image_paths)
    for i, image_path in enumerate(image_paths):
        image = Image.open(image_path)
        # Resize the image to fit in grid box
        image.thumbnail((200, 200))
        img = ImageTk.PhotoImage(image)
        image_label = tk.Label(root, image=img)
        # Keep a reference to avoid garbage collection
        image_label.image = img
        image_label.image_path = image_path
        image_label.grid(row=i // 3, column=i % 3)
        image_label.bind('<Button-1>', lambda event, path=image_path: on_image_click(path))
        images.append(image_label)

    update_image_borders()

def verify():
    print('Selected Images: ')
    selected_images_list = list()
    for img in selected_images:
        print(img[20:])
        selected_images_list.append(img[20:])
    if len(selected_images_list) == 3:
        river_images_list = ["r1.png", "r2.png", "r3.png"]
        # print(river_images_list)
        # print(selected_images_list)
        if river_images_list == sorted(selected_images_list):
            print('reCAPTCHA Authorization Successful')
            exit()
        else:
            print('reCAPTCHA Authorization Unsuccessful')
            exit()
    elif len(selected_images_list) < 3:
        print()
        print('Too few images selected. Select each river image only once and do not select mountain image.')
        print('reCAPTCHA Authorization Unsuccessful')
        exit()
    else:
        print('Too many images selected. Select each river image only once and do not select mountain image.')
        print('reCAPTCHA Authorization Unsuccessful')
        exit()
    
root = tk.Tk()
root.title("Choose the Images Which Depict a River")
selected_images = list()
create_image_grid("D:/Images_reCAPTCHA")
button_frame = tk.Frame(root)
button_frame.grid(row=(len(images) + 2) // 3, columnspan=3, pady=10)
submit_button = tk.Button(button_frame, text='Submit', command=verify)
submit_button.pack()
root.mainloop()