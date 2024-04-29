from tkinter import *
from PIL import Image, ImageTk # type: ignore
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

    phrase = "The quick brown fox jumps over the lazy dog and pack my box with five dozen liquor jugs"
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

    errorRateLabel = Label(newWindow, text="Error Rate: 0.00%", font=("Cambria", 16))
    errorRateLabel.pack(padx=(0, 50), pady=(10, 0))

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
    newWindow.errorRate = 0
    newWindow.errorCounted = False
    #Result Calculator Methods
    def start(event):
        if not newWindow.running:
            if not event.keycode in [16, 17, 18]:
                newWindow.running = True
                t = threading.Thread(target=char_calculator)
                t.start()

        if not phraseLabel.cget('text').startswith(inputtxt.get()):
            inputtxt.config(fg="red")
        else:
            inputtxt.config(fg="white")
            newWindow.errorCounted = False
        if inputtxt.get() == phraseLabel.cget('text'):
            inputtxt.config(fg="green")
            newWindow.after(1000, toResult(newWindow, newWindow.cps, newWindow.cpm, newWindow.wps, newWindow.wpm, newWindow.errorRate))
            newWindow.running = False
    
    def char_calculator():
        while newWindow.running:
            time.sleep(0.1)
            newWindow.counter += 0.1
            newWindow.cps = len(inputtxt.get()) / newWindow.counter
            newWindow.cpm = newWindow.cps * 60
            newWindow.wps =  len(inputtxt.get().split(" ")) / newWindow.counter
            newWindow.wpm = newWindow.wps * 60

            charsPerLabel.config(text=f"Characters per Second: {newWindow.cps:.2f}     Characters per Minute: {newWindow.cpm:.2f}")
            wordsPerLabel.config(text=f"Words per Second: {newWindow.wps:.2f}     Words per Minute: {newWindow.wpm:.2f}")

            total_chars = len(inputtxt.get())
            total_errors = sum(1 for i, c in enumerate(inputtxt.get()) if c != phrase[i] and i < len(phrase))
            if total_errors > newWindow.errorRate and not newWindow.errorCounted:
                newWindow.errorRate = total_errors
                newWindow.errorCounted = True
            elif total_errors < newWindow.errorRate:
                newWindow.errorCounted = False

            error_rate = newWindow.errorRate / total_chars * 100 if total_chars > 0 else 0
            errorRateLabel.config(text=f"Error Rate: {error_rate:.2f}%")

    inputtxt.bind("<KeyRelease>", start)
    
    def toResult(root, cps, cpm, wps, wpm, er):
        result.resultWindow(root, cps, cpm, wps, wpm, er)
    
    root.withdraw()