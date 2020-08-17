from tkinter import *
top = Tk()
C = Canvas(top, bg="green", height=250, width=300)
coord = 10,50,240,210
are= C.create_rectangle(coord,fill="blue")
C.pack()
top.mainloop()
