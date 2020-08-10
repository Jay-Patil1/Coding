# EXERCISE 8
# Oh Soldier Prettify My Folder.
# Paths is given .
# Take path as input.
# See all the files.
# Dictionary file, format.
# Except this,that and normal capitalise all the other files.
# Rename all the files 1-...

                # SOLUTION

'''
Author: Jay Patil
Purpose: Learning Python
'''

import os


def soldier (path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        fileList = f.read().split("\n")
    for file in files:
        if file not in fileList:
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i += 1

soldier(r"C:\Users\SHREE\Desktop\1",
        r"C:\Users\SHREE\PycharmProjects\PthonTuts\ext.txt", ".png")

