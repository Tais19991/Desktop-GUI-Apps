from tkinter import *
from PIL import ImageTk


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
        # design
        bg_color = '#F1E5D1'
        button_color = "#DBB5B5"

        # window settings
        self.title("WaterMarker")
        self.geometry('900x800')
        self.config(padx=10, pady=10, bg=bg_color)
        logo = self.set_logo("water.png")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(14, weight=1)
        self.iconphoto(False, logo)
        self.preview = None


        # main frame
        main_frame = Frame(self, bg=bg_color)
        main_frame.grid(column=0, row=0, rowspan=14, padx=10, pady=10, sticky='nsew')

        # Canvas for main_image and for logo preview on main img
        self.canvas = Canvas(main_frame, width=600, height=600, bg="blue")
        self.canvas.grid(column=0, row=0, rowspan=12, pady=10)

        self.logo_preview = Label(main_frame, bg="blue")
        self.logo_preview.grid(column=0, row=0, pady=40, padx=20)

        # Add img button
        self.add_button = Button(main_frame, text='Add your img',
                                 bg=button_color, width=80, height=2)
        self.add_button.grid(column=0, row=13, sticky=N, pady=5)

        # Save button
        save_button = Button(main_frame, text='Save result', bg=button_color, width=80, height=2)
        save_button.grid(column=0, row=14, pady=5)

        # ------------------------------------SETTINGS--------------------------------
        # Create a frame
        frame = Frame(self, bg=bg_color, padx=10, pady=10, highlightthickness=1)
        frame.grid(column=1, row=0, rowspan=14, padx=10, pady=25, sticky='N')

        # Settings button (open inner window)
        settings_button = Button(frame, width=25, height=1, bg=button_color, text="Additional settings...",
                                 command=self.create_inner_window)
        settings_button.grid(row=14, column=1, sticky=N, pady=10)

        # Text for watermark
        label = Label(frame, text='Enter text to add:', relief='flat', bg='#F1E5D1')
        label.grid(column=1, row=0, pady=5, sticky=NW)
        self.text_var = StringVar()
        self.watermark_input = Entry(frame, width=30, textvariable=self.text_var)
        self.watermark_input.grid(column=1, row=1, pady=5)
        self.watermark_input.focus()
        self.add_watermark_button = Button(frame, text='Add watermark', bg=button_color, width=25, height=1)
        self.add_watermark_button.grid(column=1, row=2, pady=5)

        # Label for text preview
        # self.text_preview = Label()
        # self.text_preview.grid(column=0, row=0, pady=10, padx=10)

        # Logo button
        self.label_logo = Label(frame, bg=bg_color)
        self.label_logo.grid(column=1, row=3, pady=15, sticky=N)
        self.add_logo_button = Button(frame, width=25, height=1, bg=button_color, text="Add your logo")
        self.add_logo_button.grid(column=1, row=4, sticky=N, pady=10)

        # Change size
        self.change_size = Scale(frame, from_=1, to=5.5, resolution=0.2, orient="horizontal",
                                 label='Size', length=180, activebackground='red',
                                 bg='#F1E5D1')
        self.change_size.grid(column=1, row=5, pady=8, sticky=N)

        # Change angle
        self.change_angle = Scale(frame, from_=0, to=90, orient="horizontal", label='Angle', length=180,
                                  activebackground='red', bg='#F1E5D1')
        self.change_angle.grid(column=1, row=6, pady=8, sticky=N)

        # Change space
        self.change_space = Scale(frame, from_=0, to=100, orient="horizontal", label='Space', length=180,
                                  activebackground='red', bg='#F1E5D1')
        self.change_space.grid(column=1, row=7, pady=8, sticky=N)

        # Change opacity
        self.change_opacity = Scale(frame, from_=255, to=0, orient="horizontal", label='Opacity', length=180,
                                    activebackground='red', bg='#F1E5D1')
        self.change_opacity.set(255)
        self.change_opacity.grid(column=1, row=8, pady=8, sticky=N)

    def set_logo(self, file_name: str):
        logo = PhotoImage(file=file_name)
        return logo

    def create_inner_window(self):
        global extra_window
        extra_window = AddWindow(self, 'inner window')

    def get_entered_text(self):
        entered_text = self.watermark_input.get()
        self.text_var.set("")  # Clear the entry
        return entered_text


class AddWindow(Toplevel):
    def __init__(self, main_window: object, label_text: str):
        super().__init__()
        self.label_text = label_text
        # Positioning
        # Get   the  main window s position and size
        root_x = main_window.winfo_x()
        root_y = main_window.winfo_y()
        # Calculate the position to place the inner window
        inner_window_x = root_x + 660
        inner_window_y = root_y + 40

        self.geometry(f"+{inner_window_x}+{inner_window_y}")

        # Add some content to the inner window
        label = Label(self, text="This is the inner window")
        label.grid(row=0, column=0, pady=20)

        # # close button
        # button_close = Button(text="Close", command=self.destroy)
        # button_close.grid(row=0, column=0, pady=10)
