# USING WITH BLOCK TO OPEN PYTHON FILE
with open("Jay.txt") as f: # No need to close the file.
    a = f.readlines()
    print(a)


# After using with block if a file is opened and all lines are read then  it reads it again.

f = open("Jay.txt","rt")
print(f.readlines())
print(f.readline())
f.close()
