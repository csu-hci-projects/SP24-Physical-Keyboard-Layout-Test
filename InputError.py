from tkinter import *


def errorWindow(root):
    newWindow = Tk()
    newWindow.title("Keyboard Layout Test - Error")
    newWindow.geometry("500x500")
    newWindow.resizable(width=False, height=False)

    header = Label(newWindow, text="You did not select a layout", font=("Cambria", 15, "bold"))
    header.place(y=10)
    header.pack()