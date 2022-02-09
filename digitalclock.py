from tkinter import *
from tkinter import font
import datetime

def quit(*args):
    window.destroy()

def clock_time():
    time= datetime.datetime.now()
    time=time.strftime('%I:%M:%S.%f %p' '\n%d-%m-%Y')
    txt.set(time)
    window.after(10,clock_time)

window=Tk()
window.title('Digital Clock')
window.geometry('1280x720')
window.resizable(True,True)
window.bind("<Escape>",quit)
window.configure(background='Black')
window.after(10,clock_time)

fnt=font.Font(family='Helvetica',size=100,weight='bold')
txt=StringVar()
# txt.set('HH:MM:SS AM')
lbl=Label(window,textvariable=txt,font=fnt,foreground='Red',background="Black")
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)


window.mainloop()