from tkinter import *
<<<<<<< HEAD
from PIL import ImageTk
=======
>>>>>>> develop


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
<<<<<<< HEAD
        # design
        bg_color = '#F1E5D1'
        button_color = "#DBB5B5"

        # window settings
        self.title("WaterMarker")
        self.geometry('900x800')
        self.config(padx=10, pady=10, bg=bg_color)
        logo = self.set_logo("water.png")
=======
        # Design features
        bg_color = '#F1E5D1'
        button_color = "#DBB5B5"

        # Window settings
        self.title("WaterMarker")
        self.geometry('900x800')
        self.config(padx=10, pady=10, bg=bg_color)
        logo = self.set_logo("assets/water.png")
        self.iconphoto(False, logo)
>>>>>>> develop
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(14, weight=1)
<<<<<<< HEAD
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
=======
        self.scales = []

        # Main frame
        main_frame = Frame(self, bg=bg_color)
        main_frame.grid(column=0, row=0, rowspan=14, padx=10, pady=10, sticky='nsew')

        # Frame for additional buttons/scales
        frame = Frame(self, bg=bg_color, padx=10, pady=10, highlightthickness=1)
        frame.grid(column=1, row=0, rowspan=14, padx=10, pady=25, sticky='N')

        # Canvas for main_image
        self.canvas = Canvas(main_frame, width=600, height=600)
        self.canvas.grid(column=0, row=0, rowspan=12, pady=10)

        # ---------------------------------BUTTONS-------------------------------------

        # Add img button
        self.add_button = Button(main_frame, text='Add main img', bg=button_color, width=80, height=2)
        self.add_button.grid(column=0, row=13, sticky=N, pady=5)

        # Save img button
        self.save_button = Button(main_frame, text='Save result', bg=button_color, width=80, height=2)
        self.save_button.grid(column=0, row=14, pady=5)

        # Clear all button
        self.clear_all = Button(frame, width=25, height=1, bg=button_color, text="Clear all changes")
        self.clear_all.grid(row=13, column=1, sticky=N, pady=10)

        # Settings button (open inner window)
        self.settings_button = Button(frame, width=25, height=1, bg=button_color, text="Additional settings...",
                                      command=self.create_inner_window)
        self.settings_button.grid(row=14, column=1, sticky=N, pady=10)

        # Upload logo button
        self.add_logo_button = Button(frame, width=25, height=1, bg=button_color, text="Add your logo")
        self.add_logo_button.grid(column=1, row=4, sticky=N, pady=10)

        # Add text for watermark button
        self.add_watermark_button = Button(frame, text='Add watermark', bg=button_color, width=25, height=1)
        self.add_watermark_button.grid(column=1, row=2, pady=5)

        # -----------------------------------LABELS--------------------------------
        # Text for watermark
        label = Label(frame, text='Enter text to add:', relief='flat', bg=bg_color)
>>>>>>> develop
        label.grid(column=1, row=0, pady=5, sticky=NW)
        self.text_var = StringVar()
        self.watermark_input = Entry(frame, width=30, textvariable=self.text_var)
        self.watermark_input.grid(column=1, row=1, pady=5)
        self.watermark_input.focus()
<<<<<<< HEAD
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
=======

        # ---------------------------------SCALES------------------------------------
        # Change size
        self.change_size = Scale(frame, from_=1, to=10,
                                 resolution=0.2,
                                 orient="horizontal",
                                 label='Size',
                                 length=180,
                                 activebackground='red',
                                 bg=bg_color)
        self.change_size.grid(column=1, row=5, pady=8, sticky=N)

        # Change angle
        self.change_angle = Scale(frame, from_=0, to=90,
                                  orient="horizontal",
                                  label='Angle',
                                  length=180,
                                  activebackground='red',
                                  bg=bg_color)
        self.change_angle.grid(column=1, row=6, pady=8, sticky=N)

        # Change opacity
        self.change_opacity = Scale(frame, from_=255, to=0,
                                    orient="horizontal",
                                    label='Opacity',
                                    length=180,
                                    activebackground='red',
                                    bg=bg_color)
        self.change_opacity.set(255)
        self.change_opacity.grid(column=1, row=7, pady=8, sticky=N)

        # Change space
        self.change_space = Scale(frame, from_=30, to=500,
                                  orient="horizontal",
                                  label='Space',
                                  length=180,
                                  activebackground='red',
                                  bg=bg_color)
        self.change_space.set(100)
        self.change_space.grid(column=1, row=8, pady=8, sticky=N)
>>>>>>> develop

    def set_logo(self, file_name: str):
        logo = PhotoImage(file=file_name)
        return logo

    def create_inner_window(self):
        global extra_window
        extra_window = AddWindow(self, 'inner window')

<<<<<<< HEAD
    def get_entered_text(self):
        entered_text = self.watermark_input.get()
        self.text_var.set("")  # Clear the entry
        return entered_text
=======
    def reset_scales(self, scales: list):
        for scale in scales:
            scale.set(scale.cget('from'))
>>>>>>> develop


class AddWindow(Toplevel):
    def __init__(self, main_window: object, label_text: str):
        super().__init__()
        self.label_text = label_text
<<<<<<< HEAD
=======
        logo = PhotoImage(file="assets/water.png")
        self.iconphoto(False, logo)

>>>>>>> develop
        # Positioning
        # Get   the  main window s position and size
        root_x = main_window.winfo_x()
        root_y = main_window.winfo_y()
        # Calculate the position to place the inner window
<<<<<<< HEAD
        inner_window_x = root_x + 660
        inner_window_y = root_y + 40
=======
        inner_window_x = root_x + 900
        inner_window_y = root_y
>>>>>>> develop

        self.geometry(f"+{inner_window_x}+{inner_window_y}")

        # Add some content to the inner window
<<<<<<< HEAD
        label = Label(self, text="This is the inner window")
        label.grid(row=0, column=0, pady=20)

        # # close button
        # button_close = Button(text="Close", command=self.destroy)
        # button_close.grid(row=0, column=0, pady=10)
=======
        label = Label(self, text="Under construction...")
        label.grid(row=0, column=0, pady=20)
>>>>>>> develop
