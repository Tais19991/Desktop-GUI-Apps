from tkinter import *


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwargs)
        return it

    def init(self, *args, **kwargs):
        pass


class MainWindow(Tk, Singleton):
    def init(self):
        super().__init__()

    def __init__(self):
        # Design features
        bg_color = "#F1F8E8"
        self.font = ("Verdana", 12, 'bold')
        self.card_front_img = PhotoImage(file='assets/card_front.png')
        self.card_back_img = PhotoImage(file='assets/card_back.png')
        self.start_button_image = PhotoImage(file="assets/button.png")

        # Window settings
        self.title("Typing Speed Test")
        self.geometry('850x750+100+10')
        self.config(padx=10, pady=10, bg=bg_color)
        self.user_input_disabled = False
        self.iconphoto(False, PhotoImage(file='assets/logo.png'))

        # Canvas text settings
        self.text_lines = []
        # self.uploaded_text_lines = []
        self.num_uploaded_lines = 0
        self.text_lines_id = []
        self.space_between_lines = 30

        # -----------------------------------------FRAMES------------------------------------------
        # Main frame
        main_frame = Frame(self, bg=bg_color)
        main_frame.grid(column=0, row=0, rowspan=14, padx=10, pady=10, sticky='nsew')

        # Frame for test result
        frame = Frame(self, bg=bg_color, padx=10, pady=10, highlightthickness=1)
        frame.grid(column=1, row=0, rowspan=14, padx=10, pady=25, sticky='N')

        # ------------------------------------CANVASES-----------------------------------------------------

        # Canvas for text example
        self.text_canvas = Canvas(main_frame, width=500, height=329)
        self.text_canvas.create_image(250, 164, image=self.card_back_img)
        self.text_canvas.create_text(230, 60, text="", font=self.font)
        self.text_canvas.config(bg=bg_color, highlightthickness=0)
        self.text_canvas.grid(column=0, row=0, rowspan=6, columnspan=2, pady=5)

        # Canvas for user's text
        self.canvas_for_input = Canvas(main_frame, width=500, height=329)
        self.canvas_for_input.create_image(250, 164, image=self.card_front_img)
        self.canvas_for_input.config(bg=bg_color, highlightthickness=0)
        self.canvas_for_input.grid(column=0, row=6, rowspan=6, columnspan=2, pady=5)

        # ------------------------------------TEXT--------------------------------------------------------
        # Widget for user input
        self.user_text_input = Text(main_frame, width=35, height=14, highlightthickness=0, wrap='word')
        self.user_text_input.config(font=self.font)
        self.user_text_input.insert('1.0', "Start typing the text you see above 🔺.\n\n"
                                           "Be prepared!\n\nThe timer will start counting as soon as you click "
                                           "on this field!")
        # self.user_text_input.insert(END, "")
        self.user_text_input.tag_add("highlight", "3.0", "3.14")
        self.user_text_input.tag_config("highlight", foreground="red")  # background="yellow"
        self.user_text_input.grid(column=0, row=6, rowspan=6)

        self.scroll_bar = Scrollbar(main_frame, command=self.user_text_input.yview)
        self.scroll_bar.grid(column=1, row=7, rowspan=4, sticky='ns')
        self.user_text_input.config(yscrollcommand=self.scroll_bar.set)

        # ---------------------------------BUTTONS----------------------------------------------
        # Restart button
        self.restart_button = Button(main_frame, width=25, height=25, image=self.start_button_image)
        self.restart_button.grid(column=0, row=14, columnspan=2, pady=2, padx=210, sticky=NE)

        # -----------------------------------LABELS-----------------------------------------------
        # Timer label
        self.timer_label = Label(main_frame, text='01:00', relief='flat', bg=bg_color, font=self.font, fg='grey')
        self.timer_label.grid(column=0, row=14, columnspan=2, pady=5, padx=200, sticky=NW)

        # Result label
        self.result_label = Label(frame, text="Your result:", relief='flat', bg=bg_color, font=self.font)
        self.result_label.grid(column=2, row=1, pady=5)

    def show_result(self, correct_typed_words: int, total_num_typed_words: int, mistakes: str) -> None:
        """Show the result on result label"""
        self.result_label.config(text="Your result: \n\n\n"
                                      f"✔ Typing speed: {correct_typed_words} word/min\n\n"
                                      f"(The average speed is 40 WPM)\n\n"
                                      f"✔ Total number of words: {total_num_typed_words}\n\n"
                                      f"✔ Mistaped words:\n"
                                      f"_____________________"
                                      f"\n\nInitial word  -  Your typo\n"
                                      f"_____________________\n"
                                      f"{mistakes}")
        self.result_label.config(justify='left', state="disabled")
        self.result_label.grid(column=2, row=0, columnspan=12, pady=5)

    def reset_timer_label(self) -> None:
        """Show initial timer label"""
        self.timer_label.config(text='01:00')

    def update_timer_label(self, min, sec) -> None:
        """Show current timer label"""
        self.timer_label.config(text=f"0{min}:{sec}")

    def define_string_dimensions(self, string: str) -> tuple:
        """Find out word width and height according to it's font"""
        canvas = Canvas()
        text_id = canvas.create_text(0, 0, text=string, font=self.font)
        bbox = canvas.bbox(text_id)
        word_width = bbox[2] - bbox[0]
        word_height = bbox[3] - bbox[1]
        canvas.update_idletasks()

        return word_width, word_height

    def prepare_text_to_fit_canvas_width(self, words_list: list) -> None:
        """ Wraps the given text to fit canvas within the specified width, returns a list of lines."""
        line = ""
        for word in words_list:
            line += word + " "
            line_width, _ = self.define_string_dimensions(line)

            if line_width < (self.text_canvas.winfo_width() - 120):
                pass
            else:
                self.text_lines.append(line.strip())
                line = ""

    def place_text_on_canvas(self) -> str:
        """Place text from self.text_lines on given canvas and return str of uploaded text"""
        uploaded_text = ''
        _, line_height = self.define_string_dimensions(self.text_lines[0])
        y = 30
        num_lines = 0
        for line in self.text_lines[self.num_uploaded_lines:]:
            text_id = self.text_canvas.create_text(240, y, text=line, font=self.font)
            self.text_lines_id.append(text_id)
            y += self.space_between_lines
            num_lines += 1
            uploaded_text += line + " "
            if (line_height + self.space_between_lines) * (num_lines - 2) > self.text_canvas.winfo_height():
                self.num_uploaded_lines += num_lines
                break

        print(uploaded_text)
        return uploaded_text

    def clear_text_from_canvas(self) -> None:
        """Clear example text canvas by text line id"""
        for id in self.text_lines_id:
            self.text_canvas.delete(id)
        self.text_lines_id.clear()

    def reset_user_text_input(self) -> None:
        """Reset input text widget to initial state"""
        self.user_text_input.config(state='normal')
        self.user_text_input.delete("1.0", "end-1c")
        self.user_text_input.insert('1.0', "Start typing the text you see above 🔺.\n\n"
                                           "Be prepared!\n\nThe timer will start counting as soon as you click "
                                           "on this field!")

    def reset_widgets(self, bind_func) -> None:
        """Reset all window's widgets to initial state"""
        # example text
        self.num_uploaded_lines = 0
        self.clear_text_from_canvas()
        self.place_text_on_canvas()
        # result label
        self.result_label.config(text="Your result:")
        # user input
        self.reset_user_text_input()
        # timer label
        self.reset_timer_label()
        self.user_text_input.bind("<Button-1>", bind_func)
