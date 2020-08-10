# OS MODULE
import os  # Operating System
print(dir(os))  # Gives the methods and attributes which can be used with the module, etc.
print(os.getcwd())  # The current working directory.
os.chdir("C://")  # This takes the program to the () location.
print(os.getcwd())
open("HarryF.txt")
print(os.listdir())  # This gives all the files in the folder.
print(os.listdir("C://"))  # This can be used for any location.
print(type(os.listdir()))  # This is a list.
os.mkdir("This/")  # A folder is created.
os.mkdir("This/that")  # Error is shown as there is no folder named This.
os.makedirs("This/that")  # This makes the folder and the sub-folder.
os.rename("MyLogs.txt", "Mylogs.txt")  # The file or folder is renamed.
os.rename("Mylogs.txt", "MyLogs.txt")
print(os.environ.get("Path"))  # The environment variables.
print(os.path.join("C://", "HarryF.txt"))  # This joins the paths directly.
print(os.path.exists("C://"))  # This give if the directory is in the path.
print(os.path.isfile("C://Program Files"))  # False as it is not a file.
print(os.path.isdir("C://Program Files"))  # True as it is a dir.
