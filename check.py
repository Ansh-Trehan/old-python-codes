from tkinter import *
top = Tk()
C1 = Checkbutton(top, text="Music", onvalue=1, offvalue=0, height=5, width=20)
C2 = Checkbutton(top, text="Video", onvalue=1, offvalue=0, height=15, width=50)
C1.pack()
C2.pack()
top.mainloop()
