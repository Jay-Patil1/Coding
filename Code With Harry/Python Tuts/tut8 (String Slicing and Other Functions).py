# STRING SLICING AND OTHER FUNCTIONS
mystr = "Jay is a good boy"
print(len(mystr))
print(mystr[0:17])
# String cans be sliced and printed using [].
# Index of the string is typed in []. * Index starts form 0
# Index range can be selected by using :.* Index before the : is included, but the index after the : is not included.
# length of the string can be printed using print(len(string name)).
# When printing string if string is not of the length then it is not printed.For eg. in mystr 78.
# but if : is used then the whole string is printed.
print(mystr[78])
# If index is written as 0:5:2 then every second index will be printed.
print(mystr[0:]) # Whole string is printed.
print(mystr[:5]) # Initial index is considered 0.
print(mystr[:]) # Whole string is printed.

# EETENDED SLICE
print(mystr[::]) # Whole string is printed.* default value for skipped printing is 1.
print(mystr[::24675]) # If index isnt available only the 0th index is printed.

# NEGATIVE INDEX
print(mystr[-4:-2]) # If index is -ve then the string is considered from the right side.
print(mystr[::-1]) # if index is negative the string will be inverted.
print(mystr[::-2]) # If index is less than -1 then the string is first inverted and then the indices are skipped.

print(mystr.isalnum()) # Prints whether the string is alphanumeric(without special characters *also space) or not.*True or False.
print(mystr.isalpha()) # Prints Whether the string is alphanumeric or not.*True or False.
print(mystr.endswith("boy")) # Prints whether the sting ends with given value in ().
print(mystr.count("o")) # Prints the number of times the given value () occurs in the string.
print(mystr.capitalize()) # Prints the string with the first letter capital.
print(mystr.find("is")) # Prints the index of the first letter in the value from the string.
print(mystr.lower()) # Prints the string is lower case.
print(mystr.upper()) # Prints the string in upper case.
print(mystr.replace("is", "are")) # prints the string with the value of the first() replace with the value of the second ().

                            # Learn more sting functions from google.
