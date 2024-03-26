from tkinter import *
from PIL import Image, ImageTk
import random


def errorTracker():
    return


def wpmTracker():
    return


def layoutImage(layout):
    if layout == "QWERTY":
        image = ImageTk.PhotoImage(Image.open('Photos/QWERTY.png'))
        return image
    elif layout == "Dvorak":
        image = ImageTk.PhotoImage(Image.open('Photos/DVORAK.png'))
        return image
    elif layout == "Colemak":
        image = ImageTk.PhotoImage(Image.open('Photos/Colemak.png'))
        return image
    elif layout == "Workman":
        image = ImageTk.PhotoImage(Image.open('Photos/Workman.png'))
        return image


def createTest(root, layout):
    # Creates Toplevel
    newWindow = Toplevel(root)
    newWindow.title("Keyboard Layout Test - " + layout)
    newWindow.geometry("1200x600")
    newWindow.resizable(width=False, height=False)

    # Enter the Phrase
    entryLabel = Label(newWindow, text="Enter the phrase below:", font=("Cambria", 15, "bold"))
    entryLabel.pack()

    # Random Phrase Generator
    phrases = {1: "the five boxing wizards jump quickly", 2: "pack my box with five dozen liquor jugs",
               3: "the quick brown fox jumps"}
    phraseLabel = Label(newWindow, text=phrases.get(random.randint(1, 3)), font=("Cambria", 25, "bold"))
    phraseLabel.pack()

    label = Label(newWindow, text="")

    label.pack(padx=(0, 25), pady=(25, 0))

    # Text Entry Box
    inputtxt = Text(newWindow, height=1, width=40, font="Cambria")
    inputtxt.pack()

    label = Label(newWindow, text="")
    label.pack(padx=(0, 50), pady=(50, 0))


    # Image of Layout
    image = layoutImage(layout)
    label = Label(newWindow, image=image)
    label.image = image
    label.pack()
