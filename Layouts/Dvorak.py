from tkinter import *

def dvorakTest(root):
    newWindow = Toplevel(root)
    newWindow.title("Keyboard Layout Test - Dvorak")
    newWindow.geometry("1200x600")
    newWindow.resizable(width=False, height=False)
    root.withdraw()