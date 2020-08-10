# SEEK(),TELL() AND MORE
f = open("Jay.txt")
print(f.tell()) # Tell the location of the file pointer.
print(f.readline())
print(f.tell())
f.seek(0) # Reads form the () character.
print(f.tell())
print(f.readline())
print(f.tell())
f.close()
