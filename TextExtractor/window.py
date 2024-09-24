import os
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo, showerror


class MainWindow(Tk):
    """Define window and widgets appearance, widget's commands"""
    def __init__(self):
        # Design features
        super().__init__()
        bg_color = "#DDE6ED"
        button_color = "#9DB2BF"
        self.font = ("Verdana", 10, 'bold')

        # Window settings
        self.title("Image in Text")
        self.geometry('1250x750+100+10')
        self.config(padx=10, pady=10, bg=bg_color)
        self.user_input_disabled = False

        # Path to save text input
        self.desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        # -----------------------------------------FRAMES------------------------------------------
        # Main frame
        main_frame = Frame(self, bg=bg_color)
        main_frame.grid(column=0, row=0, rowspan=14, padx=10, pady=20, sticky='nsew')

        # Frame for additional buttons/scales
        frame = Frame(self, bg=bg_color, highlightthickness=0)
        frame.grid(column=2, row=0, rowspan=14, padx=5, pady=24, sticky='N')

        # ------------------------------------CANVASES------------------------------------------------
        # Canvas for main_image
        self.canvas = Canvas(main_frame, width=500, height=590, bg="#526D82", highlightthickness=0)
        self.canvas.grid(column=0, row=0, rowspan=12, pady=15)

        # ------------------------------------TEXT---------------------------------------------------
        # Widget for user input
        self.user_text_input = Text(frame, width=48, height=36, highlightthickness=0, wrap='word')
        self.user_text_input.config(font=self.font)
        self.user_text_input.insert('1.0', "Text from the image will appear here (you can edit it before saving):\n\n")
        # self.user_text_input.insert(END, "")
        self.user_text_input.tag_add("highlight", "3.0", "3.14")
        self.user_text_input.tag_config("highlight", foreground="red")  # background="yellow"
        self.user_text_input.grid(column=2, row=0, padx=1, rowspan=12, pady=16)

        self.scroll_bar = Scrollbar(frame, command=self.user_text_input.yview)
        self.scroll_bar.grid(column=3, row=1, rowspan=10, sticky='ns')
        self.user_text_input.config(yscrollcommand=self.scroll_bar.set)

        # ---------------------------------BUTTONS----------------------------------------------
        # Add img button
        self.add_button = Button(main_frame, text='Add Image With Text ⬆️', width=55, height=2, font=self.font,
                                 bg=button_color)
        self.add_button.grid(column=0, row=13, sticky=N, pady=5)

        # Save text button
        self.save_button = Button(frame, text='Save Result In TXT ⬇️', width=49, height=2, font=self.font,
                                  bg=button_color)
        self.save_button.grid(column=2, row=13, pady=8)

        # Turn to text button
        self.to_text_button = Button(text='To text -> ', width=20, height=2, font=self.font, bg=button_color)
        self.to_text_button.grid(column=1, row=7, pady=8, padx=8)

        # --------------------------------CHECK BOX-------------------------------------------
        # Create IntVars for both checkboxes
        self.checkbox_en = IntVar()
        self.checkbox_ru = IntVar()

        self.check_box_en = Checkbutton(text='EN', bg=bg_color, variable=self.checkbox_en,
                                        command=lambda: self.on_checkbox_change("en"))
        self.check_box_en.grid(column=1, row=5, pady=3, padx=5)

        self.check_box_ru = Checkbutton(text='RU', bg=bg_color, variable=self.checkbox_ru,
                                        command=lambda: self.on_checkbox_change("ru"))
        self.check_box_ru.grid(column=1, row=6, pady=9, padx=5)

    def on_checkbox_change(self, val) -> None:
        """Function ensures that only one checkbox remains selected at a time"""
        if val == 'ru':
            self.checkbox_en.set(0)
        elif val == 'en':
            self.checkbox_ru.set(0)

    def find_language(self) -> str:
        """Check checkboxes and return chosen language"""
        if self.checkbox_ru.get() == 1:
            return 'rus'
        elif self.checkbox_en.get() == 1:
            return 'eng'
        else:
            return ''

    def clear_text(self) -> None:
        """Delete all text from Text widget"""
        self.user_text_input.config(state='normal')
        self.user_text_input.delete("1.0", "end-1c")

    def place_text(self, text: str) -> None:
        """Place text in Text widget"""
        self.user_text_input.insert('end', text)

    def get_corrected_text(self) -> str:
        """Get text from Text widget"""
        return self.user_text_input.get("1.0", "end-1c")

    def save_text(self) -> None:
        """Save text to user desktop in .txt or .doc format"""
        # Ask the user where to save the file
        text_to_save = self.get_corrected_text()
        file_path = filedialog.asksaveasfilename(initialdir=self.desktop_path,
                                                 title="Save a text",
                                                 defaultextension=".txt",
                                                 filetypes=(("txt files", "*.txt"),
                                                            ("word", "*.doc"),
                                                            ("word_new", "*.docx")))

        if file_path:
            with open(file_path, 'w') as f:
                f.write(text_to_save)
            showinfo(message=f"Text saved at {file_path}")
        else:
            showerror(message="Save operation cancelled.")

        # Clear img and text
        self.clear_text()
        self.canvas.delete("all")
