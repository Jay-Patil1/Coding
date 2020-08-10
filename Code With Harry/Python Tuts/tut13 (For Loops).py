# FOR LOOPS
# Loops are continuous cycles.
list1 = [["Harry",1] ,["Larry",2 ],["Carry",6], ["Marie",250]]
# For Loop
for item, lollypop  in list1: #Indention is applied for the all the list items.
    print(item,lollypop)
# If list1 is tuple then too it can be looped.
# If there are lists of list then too all the list items are printed.
dict1 = dict(list1)# Converts List to Dictionary.
print(dict1)
# for item, lollypop  in dict1.items(): # Loop for dictionary.
#     print(item,lollypop)
for item in dict1:
    print(item) # Prints only the keys of the dictionary.

# QUIZ
# Make a list. check if it is an int: check if it is greater tan 6
list2 = [1,2,3,4,5,6,"YASH",8,9,10,"JAY",12,6]
for item in  list2:
    if str(item).isnumeric() and item>6: #str(item) is used because the lsit items are in string type.
        print(item)

 
