from tkinter import *
root = Tk()
root.geometry("444x233")
root.title("Jay's GUI")

# Important Label Options
# text - adds the text 
# bg - background
# fg - foreground
# font - sets the font
# font=("comicscansms", 12, "bold")
# font="comicscansms 12 bold"
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOV, RIDGE

title_lable = Label(text='''Abdul Rashid Salim Salman Khan ; Hindi; 27 December 1965) is an Indian film actor, producer, occasional singer and television personality.
 \nIn a film career spanning over thirty years, Khan has received numerous awards, including two National Film Awards as a film producer, and two Filmfare Awards for acting.
 \nHe is cited in the media as one of the most commercially successful actors of both world and Indian cinema.
 \nForbes included him in their 2015 list of Top-Paid 100 Celebrity Entertainers in world; Khan tied with Amitabh Bachchan for No. 71 on the list, both with earnings of $33.5 million.'''
 , bg="red", fg="white", padx=50, pady=50, font="comicscansms 12 bold"
 , borderwidth=3, relief=SUNKEN)


# Important Pack Options
# anchor = n, s, e, w, ne, nw, se, sw. 
# side = top, bottom, left, right. 
# fill  Stretches the lable.
# padx
# pady

# title_lable.pack(side=BOTTOM, anchor="sw", fill=X)
title_lable.pack(side=LEFT, anchor="sw", fill=Y, padx=10, pady=10)


root.mainloop()
