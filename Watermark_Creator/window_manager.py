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
        bg_color = '#F1E5D1'
        button_color = "#DBB5B5"

        # Window settings
        self.title("WaterMarker")
        self.geometry('900x800')
        self.config(padx=10, pady=10, bg=bg_color)
        self.iconphoto(False, PhotoImage(file="assets/water.png"))
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(14, weight=1)
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
        self.add_logo_button = Button(frame, width=25, height=1, bg=button_color, text="Add logo (image)")
        self.add_logo_button.grid(column=1, row=4, sticky=N, pady=10)

        # Add text for watermark button
        self.add_watermark_button = Button(frame, text='Add text', bg=button_color, width=25, height=1)
        self.add_watermark_button.grid(column=1, row=2, pady=5)

        # -----------------------------------LABELS--------------------------------
        # Text for watermark
        label = Label(frame, text='Enter text to add:', relief='flat', bg=bg_color)
        label.grid(column=1, row=0, pady=5, sticky=NW)
        self.watermark_input = Entry(frame, width=30)
        self.watermark_input.grid(column=1, row=1, pady=5)
        self.watermark_input.focus()

        # additional label
        label = Label(frame, text="OR", relief='flat', bg=bg_color)
        label.grid(column=1, row=3, pady=5)

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

    def create_inner_window(self) -> None:
        """Create additional window"""
        global extra_window
        extra_window = AddWindow(self, 'inner window')

    def reset_scales(self) -> None:
        """Reset scales widgets to initial state"""
        scales = [self.change_size, self.change_opacity, self.change_angle]
        for scale in scales:
            scale.set(scale.cget('from'))
        self.change_space.set(100)


class AddWindow(Toplevel):
    def __init__(self, main_window: object, label_text: str):
        super().__init__()
        self.label_text = label_text
        logo = PhotoImage(file="assets/water.png")
        self.iconphoto(False, logo)

        # Positioning
        # Get   the  main window s position and size
        root_x = main_window.winfo_x()
        root_y = main_window.winfo_y()
        # Calculate the position to place the inner window

        inner_window_x = root_x + 900
        inner_window_y = root_y
        self.geometry(f"+{inner_window_x}+{inner_window_y}")

        # Add some content to the inner window
        label = Label(self, text="Under construction...")
        label.grid(row=0, column=0, pady=20)
