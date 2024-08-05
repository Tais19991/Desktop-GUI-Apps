from window_manager import MainWindow
from image_manager import *
<<<<<<< HEAD
from functools import partial
from obserwer_main import *

def ImgManager():
    pass


changed_img = None
changed_text = None


def size_changer(gain):
    global changed_img
    listener = ChangeListen()
    img = water_text_image.initial_img if changed_img is None else changed_img
    new_img = ImgSizeChanger(img, window.logo_preview)

    listener.attach(new_img)
    listener.gain = float(gain)
    changed_img = new_img.resized_img


def angle_changer(gain):
    global changed_img
    listener = ChangeListen()
    img = logo_image.resized_image if changed_img is None else changed_img
    img_angle_changer = ImgRotator(img, window.logo_preview)

    listener.attach(img_angle_changer)
    listener.gain = int(gain)
    changed_img = img_angle_changer.rotated_img

def opacity_changer(gain):
    global changed_img
    listener = ChangeListen()
    img = logo_image.resized_image if changed_img is None else changed_img
    img_opacity_changer = ImgOpacityModifier(img, window.logo_preview)

    listener.attach(img_opacity_changer)
    listener.gain = int(gain)



window = MainWindow()
main_image = ImageWaterMark()
logo_image = ImageWaterMark()
water_text_image = ImageWaterMark()



window.add_button.config(command=partial(main_image.load_image, canvas_width=600, canvas_height=600,
                                         canvas=window.canvas))

window.add_logo_button.config(command=partial(logo_image.display_label_on_canvas,
                                              label=window.label_logo,
                                              label_width=80, label_height=80,
                                              label_to_add=window.logo_preview))

window.add_watermark_button.config(command=partial(water_text_image.text_to_image, window_input=window,
                                                   label=window.logo_preview))

# Change watermark
window.change_size.config(command=lambda value: size_changer(float(value)))
window.change_angle.config(command=lambda value: angle_changer(int(value)))
window.change_opacity.config(command=lambda value: opacity_changer(int(value)))

=======
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
>>>>>>> develop

if __name__ == "__main__":
    window.mainloop()
