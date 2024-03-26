from tkinter import *
from tkinter import ttk


def qwertyTest(root):
    test = Toplevel(root)
    test.title("Keyboard Layout Test - QWERTY")
    test.geometry("1200x600")
    test.resizable(width=False, height=False)
    root.withdraw()

    entry = StringVar(test)
    textbox = ttk.Entry(test, state='readonly', textvariable=entry)
    textbox.grid(rowspan=1, columnspan=100, ipadx=999, ipady=20)


    # Row 1-1
    # Row 1-2
    # Row 1-3
    # Row 1-4
    # Row 1-5
    # Row 1-6
    # Row 1-7
    # Row 1-8
    # Row 1-9
    # Row 1-10
    # Row 1-11
    # Row 1-12
    # Row 1-13 (Back Space)

    # Row 2-1
    # Row 2-2
    # Row 2-3
    # Row 2-4
    # Row 2-5
    # Row 2-6
    # Row 2-7
    # Row 2-8
    # Row 2-9
    # Row 2-10
    # Row 2-11
    # Row 2-12
    # Row 2-13

    # Row 3-1
    # Row 3-2
    # Row 3-3
    # Row 3-4
    # Row 3-5
    # Row 3-6
    # Row 3-7
    # Row 3-8
    # Row 3-9
    # Row 3-10
    # Row 3-11
    # Row 3-12 (Enter)

    # Row 4-1
    # Row 4-2
    # Row 4-3
    # Row 4-4
    # Row 4-5
    # Row 4-6
    # Row 4-7
    # Row 4-8
    # Row 4-9
    # Row 4-10