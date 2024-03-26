from tkinter import *

import InputError as e
import LayoutTest as LT
from PIL import Image, ImageTk


def startApp(root):
    root.title("Keyboard Layout Test")
    root.geometry("1000x500")
    root.resizable(width=False, height=False)

    header = Label(root, text="Welcome to our keyboard layout test", font=("Cambria", 20, "bold"))
    header.place(y=10)
    header.pack()

    selection = Label(root, text="Please select a keyboard layout to get started", font=("Cambria", 20, "bold"))
    selection.place(y=30)
    selection.pack()

    selectedLayout = StringVar(root)
    selectedLayout.set("--Select a layout--")
    layoutMenu = OptionMenu(root, selectedLayout, "--Select a layout--", "QWERTY", "Dvorak", "Colemak", "Workman")
    layoutMenu.pack()

    def startApp():
        layout = selectedLayout.get()
        if layout == "--Select a layout--":
            e.errorWindow(root)
        else:
            LT.createTest(root, layout)

    button = Button(root, text="Start test", command=startApp)
    button.pack()

    root.mainloop()