from tkinter import *
import tkinter.ttk as ttk

import Functions as F
app= Tk()

def new_window():
    global new
    new = Toplevel()

def _1_GooGle():
    newWindow = Toplevel()
    print('구글구글')

making = Button(app,text="faf",command = _1_GooGle)
making.pack(pady="5")

app.title('adf')
app.geometry("200x59")

app.mainloop()