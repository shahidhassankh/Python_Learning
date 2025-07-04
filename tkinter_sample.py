# from tkinter import *

# window=Tk()
# Checkbutton(window).grid(row=0,column=0)
# window.mainloop()

from gtts import gTTS
import os
g=gTTS(text="rohith kuruma curry is coming stayyyyy bow bow bow stay",lang='en')
g.save("sample.mp3")


