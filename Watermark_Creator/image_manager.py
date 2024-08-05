from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
from tkinter import filedialog
import tkinter as tk


<<<<<<< HEAD
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


=======
class ImageManager:
    def __init__(self, canvas: object):
        self.desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.main_canvas = canvas
        self.img_resize_factor = None
        self.size_gain = 0
        self.angle_gain = 0
        self.opacity_gain = 0
        self.start_multi_img = 20
        self.distance_multi_img = 100
        self.image_refs = []
        self.last_updated_img = None

        # Pillow Image obj
        self._initial_img = None
        self._resized_img = None
        self._rotated_img = None
        self._transparent_img = None

        # ImageTk.PhotoImage obj
        self._preview_img = None

    @property
    def initial_img(self):
        return self._initial_img

    @initial_img.setter
    def initial_img(self, new_initial_img):
        self._initial_img = new_initial_img

    @property
    def resized_img(self):
        return self._resized_img

    @resized_img.setter
    def resized_img(self, new_resized_img):
        self._resized_img = new_resized_img

    @property
    def rotated_img(self):
        return self._rotated_img

    @rotated_img.setter
    def rotated_img(self, new_rotated_img):
        self._rotated_img = new_rotated_img

    @property
    def transparent_img(self):
        return self._transparent_img

    @transparent_img.setter
    def transparent_img(self, new_transparent_img):
        self._transparent_img = new_transparent_img

    @property
    def preview_img(self):
        return self._preview_img

    @preview_img.setter
    def preview_img(self, new_preview_img):
        self._preview_img = new_preview_img

    def load_image(self, img_resize_height, multiply: bool = False):
        self.img_resize_factor = img_resize_height
        file_path = filedialog.askopenfilename(initialdir=self.desktop_path,
                                               title="Select an image",
                                               filetypes=(("all files", "*.*"),
                                                          ("img files", "*.png"),
                                                          ("img files", "*.jpg")))
        if file_path:
            self.initial_img = Image.open(file_path).convert("RGBA")
            print(self.initial_img)
            self.resize_img()

            if not multiply:
                self.update_canvas()
            elif multiply:
                self.update_multi_img_canvas()

    def load_text(self, widget_window):
        self.initial_img = self.text_to_image(widget_window).convert('RGBA')
        self.img_resize_factor = self.initial_img.height
        self.resize_img()
        self.update_multi_img_canvas()

    def save_final_img(self, overlay_img_list: list):
        background = self.resized_img.convert("RGB")

        if not overlay_img_list:
            print("No images to overlay.")
            return

        for img in overlay_img_list:
            for item_id, _ in img.image_refs:
                coordinates = self.main_canvas.coords(item_id)
                if coordinates:
                    x, y = int(coordinates[0]), int(coordinates[1])
                    overlay = img.last_updated_img
                    if overlay.mode != 'RGBA':
                        overlay = overlay.convert('RGBA')
                    background.paste(overlay, (x, y), overlay)

        # Ask the user where to save the file
        file_path = filedialog.asksaveasfilename(initialdir=self.desktop_path,
                                                 title="Save an image",
                                                 defaultextension=".jpg",
                                                 filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png")))

        if file_path:
            background.save(file_path)
            print(f"Image saved at {file_path}")
        else:
            print("Save operation cancelled.")

    def render_overlay_img(self):
        # if self.size_gain > 0:
        self.resize_img(self.size_gain)
        # elif self.angle_gain > 0:
        self.rotate_img(self.angle_gain)
        # elif self.opacity_gain > 0:
        self.change_img_opacity(self.opacity_gain)
        self.get_preview_img()

    def get_preview_img(self):
        self.preview_img = ImageTk.PhotoImage(self.last_updated_img)

    def resize_img(self, size_gain: int = 0):
        """Resize image for preview_img in tk window"""

        # Determine new dimensions
        img_size_ratio = self.initial_img.height / self.initial_img.width
        new_height = int(self.img_resize_factor * img_size_ratio)
        new_width = int(self.img_resize_factor)

        if size_gain > 0:
            self.size_gain = size_gain
            new_height = int(new_height * size_gain)
            new_width = int(new_width * size_gain)

        # Ensure dimensions do not exceed 600x600 (window's canvas size)
        while new_height > 650 or new_width > 650:
            self.img_resize_factor /= 2
            new_height = int(self.img_resize_factor * img_size_ratio)
            new_width = int(self.img_resize_factor)

        print(f"Resizing image to {new_width}x{new_height}")

        self.resized_img = self.initial_img.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)
        self.last_updated_img = self.resized_img

    def rotate_img(self, angle_gain: int):
        """Rotate image for preview_img in tk window"""
        center_x = int(self.resized_img.width / 2)
        center_y = int(self.resized_img.height / 2)
        self.angle_gain = angle_gain

        # if img_to_change.mode != 'RGBA':
        #     img_to_change = img_to_change.convert('RGBA')

        if angle_gain is not None and angle_gain > 0:
            self.rotated_img = self.resized_img.rotate(angle_gain,
                                                       expand=True,
                                                       fillcolor=(0, 0, 0, 0),
                                                       resample=Image.Resampling.BICUBIC,
                                                       center=(center_x, center_y))
            self.last_updated_img = self.rotated_img
            # self.preview_img = ImageTk.PhotoImage(self.rotated_img)

        else:
            pass

    def change_img_opacity(self, opacity_gain: int):
        """Change image opacity for preview_img in tk window"""
        if self.rotated_img is not None:
            img_to_change = self.rotated_img.copy()
        elif self.resized_img is not None:
            img_to_change = self.resized_img.copy()
        else:
            img_to_change = self.initial_img.copy()

            # Ensure the image has an alpha channel
        if img_to_change.mode != 'RGBA':
            img_to_change = img_to_change.convert('RGBA')

        self.opacity_gain = opacity_gain
        if opacity_gain is not None and opacity_gain > 0:
            alpha = img_to_change.split()[3]
            alpha = alpha.point(lambda p: p * (opacity_gain / 255))
            img_to_change.putalpha(alpha)
            # Update the transparent image and preview image
            self.transparent_img = img_to_change
            self.last_updated_img = self.transparent_img
        else:
            pass

    def text_to_image(self, widget_window):
        font_path = 'assets/Microsoft Sans Serif.ttf'
        font_size = 20
        font = ImageFont.truetype(font_path, font_size)
        text_color = (0, 0, 0)
        text = widget_window.watermark_input.get()

        # Create a dummy image to get text size
        dummy_image = Image.new(mode='RGBA', size=(1, 1), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(dummy_image)
        text_width, text_height = int(draw.textlength(text, font=font)), font_size + 4
        self.img_resize_factor = text_height

        # Create an image with the size of the text
        new_image = Image.new(mode='RGBA', size=(text_width, text_height), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(new_image)

        # Draw the text on the image
        draw.text(xy=(0, 0), text=text, font=font, fill=text_color)
        return new_image

    def update_canvas(self):
        """Update main_canvas after main image loading"""
        self.main_canvas.delete("all")
        self.get_preview_img()
        self.main_canvas.config(width=self.preview_img.width(), height=self.preview_img.height())
        self.main_canvas.create_image(0, 0, image=self.preview_img, anchor=tk.NW)
        self.main_canvas.image = self.preview_img
        print('Updating main_canvas')

    def update_multi_img_canvas(self, distance_gain: int = None):
        """Update main_canvas after logo/text loading and auto_multiply elements"""
        print('Updating and mult main_canvas')
        main_canvas_width = self.main_canvas.winfo_width()
        main_canvas_height = self.main_canvas.winfo_height()

        # clear images
        for item_id, image in self.image_refs:
            self.main_canvas.delete(item_id)
        self.image_refs.clear()

        # check for distance gain
        if distance_gain is not None and distance_gain > 0:
            self.distance_multi_img = distance_gain

        # get changed and multiplied logo/text
        self.render_overlay_img()

        # create new batch of overloading logo/text
        for x in range(self.start_multi_img, main_canvas_width, self.distance_multi_img):
            for y in range(self.start_multi_img, main_canvas_height, self.distance_multi_img):
                item_id = self.main_canvas.create_image(x, y, image=self.preview_img, anchor=tk.NW)
                self.image_refs.append((item_id, self.preview_img))  # Keep a reference to avoid garbage collection
>>>>>>> develop
