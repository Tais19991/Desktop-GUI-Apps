from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
from tkinter import filedialog
import tkinter as tk


class ImageWaterMark:
    def __init__(self):
        self.desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        # Pillow Image obj
        self.initial_img = None
        self.resized_image = None
        # ImageTk.PhotoImage obj
        self.preview = None
        self.final_img = None

    def get_initial_img(self):
        return self.initial_img

    def get_final_img(self):
        return self.final_img

    def get_preview_img(self):
        return self.preview

    def load_image(self, canvas_width, canvas_height, canvas):
        file_path = filedialog.askopenfilename(initialdir=self.desktop_path, title="Select an image",
                                               filetypes=(("all files", "*.*"),
                                                          ("img files", "*.png"),
                                                          ("img files", "*.jpg")))
        if file_path:
            # Load the image using PIL
            self.initial_img = Image.open(file_path).convert("RGBA")
            self.resize_img(canvas_width, canvas_height)
            self.update_canvas(canvas)
            return self.initial_img

    def resize_img(self, canvas_width: int, canvas_height: int):
        """Resize image for preview in tk window"""
        # Calculate scaling factor to fit the image within the canvas dimensions
        width_ratio = canvas_width / self.initial_img.width
        height_ratio = canvas_height / self.initial_img.height
        resize_ratio = min(width_ratio, height_ratio)
        print(resize_ratio)
        print(self.initial_img.width * resize_ratio)
        print((self.initial_img.height * resize_ratio))

        # Resize the image maintaining aspect ratio
        self.resized_image = self.initial_img.resize((
            int(self.initial_img.width * resize_ratio),
            int(self.initial_img.height * resize_ratio)))  # Resize the image to fit the canvas

        self.preview = ImageTk.PhotoImage(self.resized_image)
        return self.preview

    def update_canvas(self, canvas):
        """Update canvas after image changing"""
        print('Updating canvas')
        # Clear the canvas
        canvas.delete("all")
        # Add the image to the canvas
        canvas.config(width=self.preview.width(), height=self.preview.height())
        canvas.create_image(0, 0, image=self.preview, anchor=tk.NW)
        # Keep a reference to avoid garbage collection
        canvas.image = self.preview

    def display_image_on_canvas(self, canvas_to_load, canvas_to_add, canvas_width, canvas_height):
        self.load_image(canvas_width, canvas_height, canvas_to_load)
        canvas_to_add.create_image(50, 50, anchor=tk.NW, image=self.preview)

    def load_image_on_label(self, label_width, label_height, label):
        file_path = filedialog.askopenfilename(initialdir=self.desktop_path, title="Select an image",
                                               filetypes=(("all files", "*.*"),
                                                          ("img files", "*.png"),
                                                          ("img files", "*.jpg")))
        if file_path:
            # Load the image using PIL
            self.initial_img = Image.open(file_path).convert("RGBA")
            self.resize_img(label_width, label_height)
            label.config(image=self.preview)
            return self.initial_img

    def display_label_on_canvas(self, label_width, label_height, label, label_to_add):
        self.load_image_on_label(label_width, label_height, label)
        label_to_add.config(image=self.preview)

    def text_to_image(self, label, window_input):
        font_path = 'Microsoft Sans Serif.ttf'
        font_size = 24
        text_color = (0, 0, 0)
        text = window_input.watermark_input.get()

        # Load a font
        font = ImageFont.truetype(font_path, font_size)

        # Create a dummy image to get text size
        dummy_image = Image.new('RGBA', (1, 1), (255, 255, 255, 0))
        draw = ImageDraw.Draw(dummy_image)
        text_width, text_height = int(draw.textlength(text, font=font)), font_size

        # Create an image with the size of the text
        image = Image.new('RGBA', (text_width, text_height), (255, 255, 250, 0))
        draw = ImageDraw.Draw(image)

        # Draw the text on the image
        draw.text(xy=(0, 0), text=text, font=font, fill=text_color)

        # Save img+text as initial img
        self.initial_img = image

        # Put text on  Label
        self.preview = ImageTk.PhotoImage(image)

        label.config(image=self.preview)
        label.image = self.preview  # Keep a reference to avoid garbage collection




class ImgSizeChanger:
    def __init__(self, img, img_label):
        self._original_img = img  # Store the original PIL Image
        self._img = img
        self.resized_img = None
        self.label = img_label

    def update(self, subject):
        print(f"SizeChanger: update called with gain {subject.gain}")
        if subject.gain > 0:
            new_width = new_height = int((90 * subject.gain))
            print(f"Resizing image to {new_width}x{new_height}")
            self.resized_img = self._original_img.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)
            self._img = ImageTk.PhotoImage(self.resized_img)
            self.label.config(image=self._img)
            self.label.image = self._img  # Keep a reference to avoid garbage collection


class ImgRotator:
    def __init__(self, img, img_label):
        self._original_img = img.rotate(0, expand=True)
        self._img = img
        self.label = img_label
        self.rotated_img = None

    def update(self, subject):
        print(f"ImageRotator: update called with angle {subject.gain}")
        center_x = int(self._original_img.width/2)
        center_y = int(self._original_img.height/2)

        self.rotated_img = self._original_img.rotate(subject.gain,
                                                     expand=True,
                                                     fillcolor=(255, 255, 255, 0),
                                                     resample=Image.Resampling.BICUBIC,
                                                     center=(center_x, center_y))

        self._img = ImageTk.PhotoImage(self.rotated_img)
        self.label.config(image=self._img)
        self.label.image = self._img  # Keep a reference to avoid garbage collection

class ImgOpacityModifier:
    def __init__(self, img, img_label):
        self._original_img = img.convert("RGBA")
        self._img = img
        self.label = img_label
        self.transparent_img = None

    def update(self, subject):
        print(f"Opacity: update called with opacity {subject.gain}")
        self.transparent_img = self._original_img.convert("RGBA")

        alpha = self.transparent_img.split()[3]
        alpha = alpha.point(lambda p: p * (subject.gain / 255.0))
        self.transparent_img.putalpha(alpha)

        self._img = ImageTk.PhotoImage(self.transparent_img)
        self.label.config(image=self._img)
        self.label.image = self._img  # Keep a reference to avoid garbage collection
        print(f"Image updated: {self._img}")


class ImgMultiplayer:
    def __init__(self, img, img_label):
        self._original_img = img  # Store the original PIL Image
        self._img = img
        self.label = img_label

    def update(self, subject):
        pass


