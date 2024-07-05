from window_manager import MainWindow
from image_manager import *
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


if __name__ == "__main__":
    window.mainloop()
