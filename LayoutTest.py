from tkinter import *
from PIL import Image, ImageTk # type: ignore
import random
import time
import threading
import Result as result

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
    phrases = {1: "The five boxing wizards jump quickly", 2: "Pack my box with five dozen liquor jugs",
               3: "The quick brown fox jumps over the lazy dog"}
    phrase = phrases.get(random.randint(1, 3))
    phraseLabel = Label(newWindow, text=phrase, font=("Cambria", 25, "bold"))
    phraseLabel.pack()

    # Padding
    label = Label(newWindow, text="")
    label.pack(padx=(0, 25), pady=(25, 0))

    # Text Entry Box
    inputtxt = Entry(newWindow, width=40, font=("Cambria", 24))
    inputtxt.pack()

    # Padding
    label = Label(newWindow, text="")
    label.pack(padx=(0, 50), pady=(10, 0))

    charsPerLabel = Label(newWindow, text="Characters per Second: 0.00     Characters per Minute: 0.00", font=("Cambria", 16))
    charsPerLabel.pack(padx=(0, 50), pady=(10, 0))

    wordsPerLabel = Label(newWindow, text="Words per Second: 0.00     Words per Minute: 0.00", font=("Cambria", 16))
    wordsPerLabel.pack(padx=(0, 50), pady=(10, 0))

    errorRateLabel = Label(newWindow, text="Error Rate: 0.00", font=("Cambria", 16))

    # Image of Layout
    
    image = layoutImage(layout)
    label = Label(newWindow, image=image)
    label.image = image
    label.pack()
    
    newWindow.running = False
    newWindow.counter = 0
    newWindow.totalCPS = 0
    newWindow.totalCPM = 0
    newWindow.totalWPS = 0
    newWindow.totalWPM = 0
    #Result Calculator Methods
    def start(event):
        if not newWindow.running:
            if not event.keycode in [16, 17, 18]:
                newWindow.running = True
                t = threading.Thread(target=char_calculator)
                t.start()

        if inputtxt.get() == phraseLabel.cget('text'):
            newWindow.running = False
            inputtxt.config(fg="green")

            for key, value in phrases.items():
                if value == phraseLabel.cget('text'):
                    del phrases[key]
                    break

            if phrases:
                newWindow.after(500, lambda: change_phrase(phraseLabel, phrases, inputtxt))
            else:
                newWindow.after(500, lambda: toResult())
        else:
            inputtxt.config(fg="white")
    
    def char_calculator():
        while newWindow.running:
            time.sleep(0.1)
            newWindow.counter += 0.1
            cps = len(inputtxt.get()) / newWindow.counter
            cpm = cps * 60
            wps = len(inputtxt.get().split(" ")) / newWindow.counter
            wpm = wps * 60
            charsPerLabel.config(text=f"Characters per Second: {cps:.2f}     Characters per Minute: {cpm:.2f}")
            wordsPerLabel.config(text=f"Words per Second: {wps:.2f}     Words per Minute: {wpm:.2f}")

    inputtxt.bind("<KeyRelease>", start)

    def change_phrase(label, phrases, inputtxt):
        phrase = random.choice(list(phrases.values()))
        label.config(text=phrase)
        inputtxt.delete(0, 'end')
    
    def toResult():
        result.resultWindow(newWindow)
    
    root.withdraw()