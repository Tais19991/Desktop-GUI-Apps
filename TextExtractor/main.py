# This application uses pytesseract for optical character recognition.
# pytesseract is licensed under the Apache License 2.0.
# Source: https://github.com/madmaze/pytesseract

from window import MainWindow
from image_manager import ImageManager
from text_extract import TextExtract
from tkinter.messagebox import showerror


def get_text() -> None:
    """ Extracts text from the selected image in the chosen language and displays it"""
    lang = window.find_language()

    # Check img path
    if image.img_path == "":
        showerror(title="Image Error:", message="No image to extract. Please, choose image")
    # Check language
    elif lang == "":
        showerror(title="Language Error:", message="Please, select the image text language.")

    # If img_path and lang correct - transform img to text
    else:
        try:
            text_new = text.image_to_text(image.img_path, language=lang)
            window.place_text(text_new)
        except FileNotFoundError:
            showerror(title="File Error:", message="The specified image file was not found.")
        except RuntimeError as timeout_error:
            showerror(title="Timeout Error:", message="Failed to recognize picture. Please try again.")
        except Exception as e:
            showerror(title="Unexpected Error:", message=f"An unexpected error occurred: {str(e)}")


window = MainWindow()
image = ImageManager(window.canvas)
text = TextExtract()

# Buttons config
window.add_button.config(command=image.upload_image)
window.to_text_button.config(command=get_text)
window.save_button.config(command=window.save_text)

if __name__ == "__main__":
    window.mainloop()
