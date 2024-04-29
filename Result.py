from tkinter import *

def resultWindow(root, cps, cpm, wps, wpm, er):
    resultWindow = Toplevel(root)
    resultWindow.title("Keyboard Layout Test - Result")
    resultWindow.geometry("1000x500")
    resultWindow.resizable(width=False, height=False)

    resultLabel = Label(resultWindow, text="Your Results", font=("Cambria", 25))
    resultLabel.pack()

    cpsLabel = Label(resultWindow, text=f"Characters per Second: {cps:.2f}", font=("Cambria", 16))
    cpsLabel.pack()

    cpmLabel = Label(resultWindow, text=f"Characters per Minute: {cpm:.2f}", font=("Cambria", 16))
    cpmLabel.pack()

    wpsLabel = Label(resultWindow, text=f"Words per Second: {wps:.2f}", font=("Cambria", 16))
    wpsLabel.pack()

    wpmLabel = Label(resultWindow, text=f"Words per Minute: {wpm:.2f}", font=("Cambria", 16))
    wpmLabel.pack()

    errorLabel = Label(resultWindow, text=f"Error Rate: {er:.2f}%", font=("Cambria", 16))
    errorLabel.pack()

    
    root.withdraw()