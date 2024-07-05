from window_manager import MainWindow
from image_manager import *
from functools import partial
from obserwer_main import *

window = MainWindow()

# Images to work with
main_image = ImageManager(canvas=window.canvas)   #
logo_image = ImageManager(canvas=window.canvas)
water_text_image = ImageManager(canvas=window.canvas)

# def get_canvas_position(main_window: object, main_img: object, img: object) -> tuple:
#     canvas_x  = main_window.winfo_rootx() + main_img.main_canvas.winfo_x() + img.main_canvas.winfo_x()
#     canvas_y = main_window.winfo_rooty() + main_img.main_canvas.winfo_y() + img.main_canvas.winfo_y()
#     return (canvas_x, canvas_y)
#
# logo_image_position = get_canvas_position(window, main_image, logo_image)
# text_image_position = get_canvas_position(window, main_image, water_text_image)

# Buttons config
window.add_button.config(command=partial(main_image.load_image, img_resize_height=600))
window.add_logo_button.config(command=partial(logo_image.load_image, img_resize_height=35, multiply=True))
window.add_watermark_button.config(command=partial(water_text_image.text_to_image, window_input=window))
# window.save_button.config(command=partial(main_image.save_final_img,
#                                           img_1=logo_image,
#                                           img_2=water_text_image,
#                                           img_1_position=logo_image_position,
#                                           img_2_position=text_image_position))

IMG_TO_CHANGE = [logo_image]


def size_changer(gain):
    for img in IMG_TO_CHANGE:
        listener = ChangeListen()
        new_img = ImgSizeChanger(img)
        listener.attach(new_img)
        listener.gain = float(gain)


def angle_changer(gain):
    for img in IMG_TO_CHANGE:
        listener = ChangeListen()
        rotated_img = ImgRotator(img)
        listener.attach(rotated_img)
        listener.gain = int(gain)


def opacity_changer(gain):
    for img in IMG_TO_CHANGE:
        listener = ChangeListen()
        img_opacity_changer = ImgOpacityModifier(img)
        listener.attach(img_opacity_changer)
        listener.gain = int(gain)

def space_changer(gain):
    for img in IMG_TO_CHANGE:
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
