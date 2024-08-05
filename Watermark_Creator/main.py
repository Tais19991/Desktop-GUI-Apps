from window_manager import MainWindow
from image_manager import *
from obserwer_main import *
from image_processing import *
from functools import partial
from event_listener import *

window = MainWindow()

# Images to work with
main_image = ImageManager(canvas=window.canvas)
logo_image = ImageManager(canvas=window.canvas)
water_text = ImageManager(canvas=window.canvas)


def check_img_obj():
    img_to_change = [img for img in (logo_image, water_text) if img.initial_img is not None]
    print(f"images to change - {img_to_change}")
    return img_to_change


# Buttons config
window.add_button.config(command=partial(main_image.load_image, img_resize_height=450))
window.add_logo_button.config(command=partial(logo_image.load_image, img_resize_height=35, multiply=True))
window.add_watermark_button.config(command=partial(water_text.load_text, widget_window=window))
window.save_button.config(command=partial(main_image.save_final_img, overlay_img_list=[logo_image, water_text]))
window.clear_all.config()

def size_changer(gain):
    for img in check_img_obj():
        listener = ChangeListen()
        new_img = ImgSizeChanger(img)
        listener.attach(new_img)
        listener.gain = float(gain)


def angle_changer(gain):
    for img in check_img_obj():
        listener = ChangeListen()
        rotated_img = ImgRotator(img)
        listener.attach(rotated_img)
        listener.gain = int(gain)


def opacity_changer(gain):
    for img in check_img_obj():
        listener = ChangeListen()
        img_opacity_changer = ImgOpacityModifier(img)
        listener.attach(img_opacity_changer)
        listener.gain = int(gain)


def space_changer(gain):
    for img in check_img_obj():
        listener = ChangeListen()
        img_space_changer = ImgSpacer(img)
        listener.attach(img_space_changer)
        listener.gain = int(gain)


# Change img/watermark
window.change_size.config(command=lambda value: size_changer(float(value)))
window.change_angle.config(command=lambda value: angle_changer(int(value)))
window.change_opacity.config(command=lambda value: opacity_changer(int(value)))
window.change_space.config(command=lambda value: space_changer(int(value)))


if __name__ == "__main__":
    window.mainloop()
