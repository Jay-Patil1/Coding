# OPEN(), READ() AND READLINE() FOR READING FILE.
open("Jay.txt") # Used to open a file.
f = open("Jay.txt","rt") # File pointer (file handle).We can use this to access the file.After the comma the file mode is written.
content = f.read(3) # The value in() is the No. of characters to be read.
print(content)
content = f.read(3) # If it is used continuously them it reads the further characters.
print(content)
f.close() # Closes the file.
# The file should to closed at the end as the resources are freed after closing.
# If read() value is more than the No. of characters in the file then it prints all the characters.
content = f.read(34455) # If the character limit exceeds all the characters are printed.
print("1",content)
content = f.read(34455) # Here this function is ignored as the characters are finished in the first one.
print("2",content) # noting is printed after 2.
f.close() # Closes the file.
for line in f:  # Prints the content line by line.
    print(line, end="")
print(f.readline()) # The new line character is also printed.
print(f.readline())
print(f.readlines()) # Prints the lines as a list.
