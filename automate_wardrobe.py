import os
import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

WINDOW_TITLE = "Panda's wardrobe"
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 220
IMG_WIDTH = 250
IMG_HEIGHT = 250

# Access file without hidden ones

ALL_TOPS = [str('tops/') + imageFile for imageFile in os.listdir("tops/") if not imageFile.startswith('.')]
ALL_BOTTOMS = [str('bottoms/') + imageFile for imageFile in os.listdir("bottoms/") if not imageFile.startswith('.')]


class WardrobeApp:
    def __init__(self, root):
        self.root = root
        # show top image
        # TOP
        self.top_images = ALL_TOPS
        # save single top
        self.top_images_path = self.top_images[0]
        # create and add top image into frame
        self.tops_frame = tk.Frame(self.root)
        self.top_image_label = self.create_photos(self.top_images_path,
                                                  self.tops_frame)
        self.top_image_label.pack(side=tk.TOP)
        self.tops_frame.pack(fill=tk.BOTH, expand=tk.YES)

        # BOTTOM
        self.bottom_images = ALL_BOTTOMS
        # save single top
        self.bottom_images_path = self.bottom_images[0]
        # create and add top image into frame
        self.bottoms_frame = tk.Frame(self.root)
        self.bottom_image_label = self.create_photos(self.bottom_images_path,
                                                     self.bottoms_frame)
        self.bottom_image_label.pack(side=tk.BOTTOM)
        self.bottoms_frame.pack(fill=tk.BOTH, expand=tk.YES)
        # create background
        self.create_background()

    def create_background(self):
        # add the title and change the size
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{}x{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
        # add all buttons
        self.create_buttons()

    def create_buttons(self):
        top_prev_button = tk.Button(self.tops_frame, text='Previous', anchor=tk.CENTER, command=self.get_prev_top)
        top_prev_button.pack(side=tk.LEFT)
        top_next_button = tk.Button(self.tops_frame, text='Next', anchor=tk.CENTER, command=self.get_next_top)
        top_next_button.pack(side=tk.RIGHT)

    def _get_next_item(self, category, current_index, increment=True):
        item_index = category.index(current_index)
        final_index = len(category)-1
        next_index = 0

        if increment and item_index == final_index:
            next_index = 0
        elif not increment and item_index == 0:
            next_index = final_index
        else:
            increment = 1 if increment else -1
            next_index = item_index + increment

        next_image = category[next_index]

        # reset image based on next_image
        if current_index in self.top_images:
            image_label = self.top_image_label
            self.top_images_path = next_image
        else:
            image_label = self.bottom_image_label
            self.bottom_images_path = next_image

            # update the photo
        self.update_photos(next_image, image_label)
        current_index = next_index

    def get_next_top(self):
        self._get_next_item(category=self.top_images, current_index=self.top_images_path, increment=True)

    def get_prev_top(self):
        self._get_next_item(category=self.top_images, current_index=self.top_images_path, increment=False)

    def get_next_bottom(self):
        self._get_next_item(category=self.bottom_images, current_index=self.bottom_image_path, increment=True)

    def get_prev_bottom(self):
        self._get_next_item(category=self.bottom_images, current_index=self.bottom_image_path, increment=False)

    def update_photos(self, new_image, image_label):
        new_image_file = Image.open(new_image)
        image = new_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo

    def create_photos(self, image_path, frame):
        image_file = Image.open(image_path)
        image_resized = image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        tk_photo = ImageTk.PhotoImage(image_resized)
        image_label = tk.Label(frame, image=tk_photo, anchor=tk.CENTER)
        image_label.image = tk_photo
        return image_label


root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()
