# DICTIONARY AND ITS FUNCTIONS
# Dictionary is nothing but key value pairs.
# Value of a dictionary can be a (list,dictionary,tupel,etc).
# Preferabely the dictionary keys should be Immutable(cannot be changed.[string,No.]).
d1 = {} # Creates Blank dictionary.
print(type(d1))
d2 = {"Harry":"Burger", "Jay":"Roti",
      "Shubham":{"B":"Maggie","L":"Roti"}}
print(d2) # Prints the dictionary.
print(d2["Jay"]) # Prints Value of Key.*If Value is searched (ERROR).
print(d2["Shubham"]) # Prints the value of "Shubham" which is a dictinary.
print(d2["Shubham"]["B"]) # Prints the value of the key form the internal dictionary.

# To increase the dictionary.
d2["Ankit"] = "Junk Food" # Adds Key and Value.
d2["Ankit"] = "JUNK FOOD" # Edits Key/Value.
print(d2)
del d2 ["Ankit"] # Deletes Key with the value.
d3 = d2 # The dictionari is renamed as d3. No new dictionary is formed.
del d3["Jay"]
print(d2)
d3 = d2.copy()# Other dictionary with same keys and values is created.
del d3["Jay"]
print(d2)
print(d3)

print(d2.get("Jay")) # Gets the value of the given key().
d2.update({"Leena":"Toffee"}) # Adds Key and Value to the dictionary.
print(d2)

print(d2.keys()) # Prints all the keys of the dictionary.
print(d2.items()) # Prints the (Key,Value) pairs.

                   # Learn python dictionary functions from google.



