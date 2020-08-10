from tkinter import *

imaginary_tech_root = Tk()

imaginary_tech_root.geometry("444x234")  # Width x Height
imaginary_tech_root.minsize(200,100)  # Width, Height
imaginary_tech_root.maxsize(795,845)  # Width, Height

Jay = Label(text="Jay is a good boy and this is his GUI")
Jay.pack()

imaginary_tech_root.mainloop()