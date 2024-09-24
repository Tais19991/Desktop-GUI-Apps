from PIL import Image, ImageTk
import os
from tkinter import filedialog
import tkinter as tk


class ImageManager:
    """Upload, get preview img and update canvas after each uploading"""
    def __init__(self, canvas: object):
        self.desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.main_canvas = canvas
        self.img_path = ''

        # Pillow Image obj
        self._initial_img = None
        # ImageTk.PhotoImage obj
        self._preview_img = None

    def upload_image(self) -> None:
        """Upload image from user desktop, resize  it for preview """
        file_path = filedialog.askopenfilename(initialdir=self.desktop_path,
                                               title="Select an image",
                                               filetypes=(("all files", "*.*"),
                                                          ("img files", "*.png"),
                                                          ("img files", "*.jpg")))
        if file_path:
            self._initial_img = Image.open(file_path).convert("RGBA")
            self.resize_img()
            self.update_canvas()
        print(file_path)
        print(type(file_path))
        self.img_path = file_path

    def resize_img(self) -> None:
        """Resize image and turn it to preview_img for tk window"""
        # Determine new dimensions
        img_size_ratio = self._initial_img.height / self._initial_img.width
        new_height = int(450 * img_size_ratio)
        new_width = 450

        resized_img = self._initial_img.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)
        self._preview_img = ImageTk.PhotoImage(resized_img)

    def update_canvas(self) -> None:
        """Update main_canvas after image loading"""
        self.main_canvas.delete("all")
        self.main_canvas.create_image(250, 295, image=self._preview_img, anchor=tk.CENTER)
        self.main_canvas.image = self._preview_img
