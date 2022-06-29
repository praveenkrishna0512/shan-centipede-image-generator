from tkinter import *
from PIL import Image, EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs9.56.1\bin\gswin64c.exe'

def save_as_png(canvas, fileName):
    # save postscipt image 
    canvas.postscript(file = fileName + '.eps') 
    # use PIL to convert to PNG 
    img = Image.open(fileName + '.eps') 
    img.save(fileName + '.png', 'png') 

root = Tk()

canvas = Canvas(root)
canvas.create_rectangle(10,10,50,50)
canvas.pack()

canvas.update()
save_as_png(canvas, "testFile")

root.mainloop()