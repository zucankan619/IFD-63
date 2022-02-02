from tkinter import *
from tkinter import font
import datetime

def quit(*args):
    window.destroy()

def clock_time():
    time= datetime.datetime.now()
    time=time.strftime('%I:%M:%S %p')
    txt.set(time)
    window.after(100,clock_time)

window=Tk()
window.title('Digital Clock')
window.geometry('1200x200')
window.resizable(False,False)
window.bind("<Escape>",quit)
window.configure(background='green')
window.after(100,clock_time)

fnt=font.Font(family='Helvetica',size=120,weight='bold')
txt=StringVar()
# txt.set('HH:MM:SS AM')
lbl=Label(window,textvariable=txt,font=fnt,foreground='White',background="Green")
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)


window.mainloop()