from tkinter import *

import InputError as e
import LayoutTest as LT
from PIL import Image, ImageTk


def startApp(root):
    root.title("Keyboard Layout Test")
    root.geometry("1000x500")
    root.resizable(width=False, height=False)

    label = Label(root, text="")
    label.pack(padx=(0, 50), pady=(50, 0))

    header = Label(root, text="Welcome to our keyboard layout test", font=("Cambria", 20, "bold"))
    header.place(y=10)
    header.pack()

    label = Label(root, text="")
    label.pack(padx=(0, 10), pady=(10, 0))

    selection = Label(root, text="Please select a keyboard layout to get started", font=("Cambria", 20, "bold"))
    selection.place(y=30)
    selection.pack()

    label = Label(root, text="")
    label.pack(padx=(0, 10), pady=(10, 0))

    selectedLayout = StringVar(root)
    selectedLayout.set("--Select a layout--")
    layoutMenu = OptionMenu(root, selectedLayout, "--Select a layout--", "QWERTY", "Dvorak", "Colemak", "Workman")
    layoutMenu.pack()

    label = Label(root, text="")
    label.pack(padx=(0, 5), pady=(5, 0))

    def startApp():
        layout = selectedLayout.get()
        if layout == "--Select a layout--":
            e.errorWindow(root)
        else:
            LT.createTest(root, layout)

    button = Button(root, text="Start test", command=startApp)
    button.pack()

    root.mainloop()