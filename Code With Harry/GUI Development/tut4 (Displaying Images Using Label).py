from tkinter import *
from PIL import Image, ImageTk

mahmudul_root = Tk()

mahmudul_root.geometry("957x604")
# photo = PhotoImage(file="Untitled.png")

# For images other than png
image = Image.open("Covid19.ico")
photo = ImageTk.PhotoImage(image)


varun_label = Label(image=photo)
varun_label.pack()


mahmudul_root.mainloop()
