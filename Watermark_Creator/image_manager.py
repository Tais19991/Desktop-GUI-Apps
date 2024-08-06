from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
from tkinter import filedialog
import tkinter as tk


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
        """Upload image from user desktop, resize and multiply (if needed) it for preview """
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
        """Upload text as overlay image"""
        self.initial_img = self.text_to_image(widget_window).convert('RGBA')
        self.img_resize_factor = self.initial_img.height
        self.resize_img()
        self.update_multi_img_canvas()

    def save_final_img(self, overlay_img_list: list):
        """Save initial main image with watermark/logo overlay according to scale"""
        background = self.initial_img.convert("RGB")
        scaling_factor = self.initial_img.height / self.resized_img.height
        print(f"scaling factor - {scaling_factor}")

        if not overlay_img_list:
            print("No images to overlay.")
            return

        for img in overlay_img_list:
            for item_id, _ in img.image_refs:
                coordinates = self.main_canvas.coords(item_id)
                if coordinates:
                    x, y = round(int(coordinates[0]) * scaling_factor), round(int(coordinates[1]) * scaling_factor)
                    overlay = img.last_updated_img.resize((int(img.last_updated_img.height * scaling_factor),
                                                           int(img.last_updated_img.width * scaling_factor)),
                                                          resample=Image.Resampling.LANCZOS)
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
        """Update overlay images (size, angle, opacity) for preview according to last gains (from listener)"""
        try:
            self.resize_img(self.size_gain)
        except AttributeError:
            print('No watermark to work with')
            pass

        self.rotate_img(self.angle_gain)
        self.change_img_opacity(self.opacity_gain)
        self.get_preview_img()

    def get_preview_img(self):
        """Get PhotoImage object to preview image"""
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

    def text_to_image(self, widget_window):
        """Get text from Enter widget and turn it into image"""
        # Text settings (can be extended)
        font_path = 'assets/Microsoft Sans Serif.ttf'
        font_size = 20
        font = ImageFont.truetype(font_path, font_size)
        text_color = (0, 0, 0)

        # Get text
        text = widget_window.watermark_input.get()
        if text == '':
            text = 'Enter your text'

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
