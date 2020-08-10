# LISTS AND LIST FUNCTIONS
# List is simply a list.
grocery = ["Harpic", "Vim", "Deoderant","Bhindi"] # Mixed list. with both integer and string.
print(grocery) # Prints the list.
print(grocery[1]) # List item No. [] is printed.*List item No. starts form 0.
numbers = [2,3,4,6,10,15]
print(numbers) # Prints the list.
print(numbers[2]) # Prints List item No. [].
numbers.sort() # Arranges the list in ascending order.
numbers.reverse() # Arranges the list in descending order.
print(numbers[0:4]) # Prints whole list.
print(numbers[0:]) # Prints whole list. Last index is considered.
print(numbers[:5]) # Initial index is considered 0.
print(numbers[:]) # Prints whole list.
#  Sort and Reverse like functions change the original list.
# Others like print([]),etc. dont change the original list.

# EXTENDED SLICCE
print(numbers[::]) # Prints whole list.
print(numbers[:4:]) # Default extended slice is 1. # default first slice is 0.
print(numbers[0:4:2]) # Prints Skipping 2 indices.
print(numbers[0::-1]) # As extended slice is -ve the list gets reversed. # Default value of second slice is maximum No. of list items.
print(len(numbers)) # Prints No. of list items.
print(max(grocery)) # Prints maximum value fromt the list items.
print(min(grocery)) # Prints minimum value from list items.
numbers.append(12) # Adds the value () as list item to the list.
# No. of appendages are unlimited.
numbers = [] # Creates Empty list.
numbers.insert(1, 67) # Insetrs the value after, after the list index No. before ,.
numbers.remove(9) # Removes the value() form the list.
numbers.pop() # Removes the last list item.
numbers[1] = 23 # Changes list index No. [] to the value.
                      # TUPLE.immutable (cannot be chanced.)
tp = (1, 2, 3) # Creates Tuple.
tp1 =(1, ) # Insert comma to make it a tuple.

                          # SWAPPING VALUES
a = 1
b = 8
temp = a
a = b
b = temp
print(a,b)
    # OR
A = 2
B = 4
A, B = B, A
print(A,B)

                     # Learn Python list functions fron google.
