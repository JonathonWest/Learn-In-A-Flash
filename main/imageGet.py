import os
from tkinter import PhotoImage
import tkinter as tk
from tkinter import font

def getTitle():
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    
    img = parent_directory+"\\resources\\title.png"

    image = PhotoImage(file=img)
    return image

def getloadanstufFlash():
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    
    img = parent_directory+"\\resources\\loadflash.png"
    img2 = parent_directory+"\\resources\\stuflash.png"

    image = PhotoImage(file=img)
    image2 = PhotoImage(file=img2)
    return image,image2



