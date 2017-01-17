
from Tkinter import *

window = Tk()

window.geometry("640x480")

import random

secret = random.randint(1, 20)
print secret

greeting = Label(window, text="Guess the secret number!")
greeting.pack(side="top") #pack verhaelt sich wie blockelement top ist default auch moeglich: bottom

labelText = StringVar()
label = Label(window, textvariable = labelText)
label.pack()
labelText.set("Guess a number between 1 and 20?")

textfeld = Entry(window)
textfeld.pack()


def EnterButton():
    while True:
        guess=int(textfeld.get())
        if guess == secret:
            labelText.set("Congratulations! You guessed correctly!")
            break
        elif guess > 20 or guess < 1:
            labelText.set("Please pick a number between 1 and 20")
        elif guess < secret:
            labelText.set("No the secret number is bigger than " + str(guess))
        elif guess > secret:
            labelText.set("No the secret number is smaller than " + str(guess))

EnterButton = Button(window, text="Guess", command=EnterButton )
EnterButton.pack()



window.mainloop()