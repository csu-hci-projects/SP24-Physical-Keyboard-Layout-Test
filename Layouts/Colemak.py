from tkinter import *

def colemakTest(root):
    newWindow = Toplevel(root)
    newWindow.title("Keyboard Layout Test - QWERTY")
    newWindow.geometry("1200x600")
    newWindow.resizable(width=False, height=False)
    root.withdraw()