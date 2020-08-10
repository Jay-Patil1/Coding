# WRITING AND APPENDING TO A FILE
f = open("Jay.txt", "w") # Use to empty the file and add the content.
f.write("Jay is a good boy\n") # Empties the content of the file adds the content in().
f.close()
f = open("Jay.txt", "a") # a is used to append to the file.
f.write("Jay is a good boy\n") # Appends the value() to the file.
f = open("Jay.txt","w")
a = f.write("Jay is a good boy.\n") # Gives the No. of characters written in the file.
print(a)
f.close()

# Handle read and write both.
f = open("Jay.txt","r+") # Open a file in both read and write modes.
print(f.read())
f.write("Thank You") # Used to write content to the file.
print(f.read())
