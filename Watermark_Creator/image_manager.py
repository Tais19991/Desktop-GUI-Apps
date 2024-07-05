from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
from tkinter import filedialog
import tkinter as tk


class ImageManager:
    def __init__(self, canvas: object = None):
        self.desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.main_canvas = tk.Canvas() if canvas is None else canvas
        self.overlay_canvases = []
        # self.main_canvas.after(100, self.set_initial_canvas_height)
        self.img_resize_factor = None
        # Add  images at  specific  coordinates
        self.image_refs = []


        # Pillow Image obj
        self._initial_img = None
        self._resized_img = None
        self._rotated_img = None
        self._transparent_img = None

        # ImageTk.PhotoImage obj
        self._preview_img = None
        self._final_img = None

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
            self.resize_img_for_preview()
            if not multiply:
                self.update_canvas()
            elif multiply:
                self.update_multy_img_canvas()

    def save_final_img(self, img_1, img_2, img_1_position: tuple, img_2_position: tuple):
        background = self.resized_img.convert("RGB")
        overlay1 = img_1.resized_img
        overlay2 = img_2.resized_img
        background.paste(overlay1, img_1_position, overlay1)
        background.paste(overlay2, img_2_position, overlay2)

        # Ask the user where to save the file
        file_path = filedialog.asksaveasfilename(initialdir=self.desktop_path,
                                                 title="Save an image",
                                                 defaultextension=".jpg",
                                                 filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png")))

        if file_path:
            background.save(file_path)

    # def set_initial_canvas_height(self):
    #     self.initial_canvas_height = self.main_canvas.winfo_height()
    #     print(f"Canvas height - {self.initial_canvas_height}")

    def resize_img_for_preview(self, gain: int = None):
        """Resize image for preview_img in tk window"""
        new_width = 0
        new_height = 0

        img_size_ratio = self.initial_img.height / self.initial_img.width
        if gain is None:
            new_height = int(self.img_resize_factor * img_size_ratio)
            new_width = int(self.img_resize_factor)
        elif gain > 0:
            new_height = int(self.img_resize_factor * img_size_ratio * gain)
            new_width = int(self.img_resize_factor * gain)

        print(f"Resizing image to {new_width}x{new_height}")
        self.resized_img = self.initial_img.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)
        self.preview_img = ImageTk.PhotoImage(self.resized_img)

    def rotate_img(self, gain: int):
        """Rotate image for preview_img in tk window"""
        center_x = int(self.resized_img.width / 2)
        center_y = int(self.resized_img.height / 2)

        if self.resized_img.mode != 'RGBA':
            self.resized_img = self.resized_img.convert('RGBA')

        self.rotated_img = self.resized_img.convert("RGBA").rotate(gain,
                                                                   expand=True,
                                                                   fillcolor=(255, 255, 255, 0),
                                                                   resample=Image.Resampling.BICUBIC,
                                                                   center=(center_x, center_y))

        self.preview_img = ImageTk.PhotoImage(self.rotated_img)

    def change_img_opacity(self, gain: int):
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

        alpha = img_to_change.split()[3]
        alpha = alpha.point(lambda p: p * (gain / 255))
        img_to_change.putalpha(alpha)

        # Update the transparent image and preview image
        self._transparent_img = img_to_change
        self.preview_img = ImageTk.PhotoImage(self._transparent_img)

    def update_canvas(self):
        """Update main_canvas after image changing"""
        self.main_canvas.delete("all")
        self.main_canvas.config(width=self.preview_img.width(), height=self.preview_img.height())
        self.main_canvas.create_image(0, 0, image=self.preview_img, anchor=tk.NW)
        self.main_canvas.image = self.preview_img
        print('Updating main_canvas')

    def update_multy_img_canvas(self, step=100):
        print('Updating and mult main_canvas')
        main_canvas_width = self.main_canvas.winfo_width()
        main_canvas_height = self.main_canvas.winfo_height()
        transparent_image = Image.new('RGBA', (main_canvas_width, main_canvas_height), (255, 255, 255, 0))
        self._transparent_img = ImageTk.PhotoImage(transparent_image)
        # self.overlay_canvas.delete("all")
        # self.main_canvas.config(width=main_canvas_width, height=main_canvas_height)
        # self.overlay_canvas = tk.Canvas(width=main_canvas_width, height=main_canvas_height)
        # self.overlay_canvas.create_image(0, 0, image=self._transparent_img, anchor=tk.NW)
        # self.overlay_canvas.image = self._transparent_img
        # self.overlay_canvas.place(x=10, y=15)
        # print("transparent image created")
        # Clear previous references
        previous_step = 100

        self.image_refs.clear()


        for canvas in self.overlay_canvases:
            canvas.destroy()


        # create new batch of canvases and pictures
        for x in range(30, main_canvas_width, step):
            for y in range(30, main_canvas_height, step):
                # overlay_canvas = tk.Canvas(width=self.preview_img.width(), height=self.preview_img.height())
                # overlay_canvas.create_image(0, 0, image=self._transparent_img, anchor=tk.NW)
                # overlay_canvas.image = self._transparent_img
                # overlay_canvas.place(x=x, y=y)
                # img_item = overlay_canvas.create_image(0, 0, image=self.preview_img, anchor=tk.NW)
                # self.overlay_canvases.append(overlay_canvas)
                overlay_canvas = tk.Label(image=self._transparent_img)
                overlay_canvas.image = self._transparent_img
                overlay_canvas = tk.Label(image=self.preview_img)
                overlay_canvas.place(x=x, y=y)
                self.overlay_canvases.append(overlay_canvas)

                self.image_refs.append((overlay_canvas, self.preview_img))  # Keep a reference to avoid garbage collection


    def text_to_image(self, window_input):
        font_path = 'Microsoft Sans Serif.ttf'
        font_size = 20
        text_color = (0, 0, 0)
        text = window_input.watermark_input.get()

        # Load a font
        font = ImageFont.truetype(font_path, font_size)

        # Create a dummy image to get text size
        dummy_image = Image.new(mode='RGBA', size=(1, 1), color=(255, 255, 255, 0))
        draw = ImageDraw.Draw(dummy_image)
        text_width, text_height = int(draw.textlength(text, font=font)), font_size

        # Create an image with the size of the text
        image = Image.new(mode='RGBA', size=(text_width, text_height), color=(255, 255, 250, 0))
        draw = ImageDraw.Draw(image)

        # Draw the text on the image
        draw.text(xy=(0, 0), text=text, font=font, fill=text_color)

        # Save img+text as initial img
        self.initial_img = image
        self.resize_img_for_preview()
        self.update_canvas()


class ImgSizeChanger:
    def __init__(self, image: object):
        self.img = image

    def update(self, subject):
        print(f"SizeChanger: update called with gain {subject.gain}")
        self.img.resize_img_for_preview(gain=subject.gain)
        self.img.update_multy_img_canvas()


class ImgRotator:
    def __init__(self, image: object):
        self.img = image

    def update(self, subject):
        print(f"ImgRotator: update called with angle -  {subject.gain}")
        self.img.rotate_img(subject.gain)
        self.img.update_multy_img_canvas()


class ImgOpacityModifier:
    def __init__(self, image: object):
        self.img = image

    def update(self, subject):
        print(f"Opacity: update called with opacity {subject.gain}")
        self.img.change_img_opacity(subject.gain)
        self.img.update_multy_img_canvas()


class ImgSpacer:
    def __init__(self, image: object):
        self.img = image

    def update(self, subject):
        print(f"Change space: update called with space {subject.gain}")
        self.img.update_multy_img_canvas(step=subject.gain)
