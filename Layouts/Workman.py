from tkinter import *

def workmanTest(root):
    newWindow = Toplevel(root)
    newWindow.title("Keyboard Layout Test - Workman")
    newWindow.geometry("1200x600")
    newWindow.resizable(width=False, height=False)
    root.withdraw()