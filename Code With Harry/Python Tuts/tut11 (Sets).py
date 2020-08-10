# SETS
s = set() # Maeks an empty set. Set is a collection of well defined objects.
# l = [1,2,3,4] #A List.
# s_from_list = set(l) # List gets converted into a set.
# print(s_from_list) # The set is printed.
# print(type(s_from_list)) # The list has become a Set.
# print(type(s))
# s_from_list = set([1,2,3,4]) # List in Set.
# print(s_from_list) # Prints the list in the set.
# print(type(s_from_list)) #The list is a Set.

          # ADDING ELEMENTS TO A SET.
s.add(1) # The value () is added to the set.
s.add(3) # If the same value is added to the set for many times its senn just once.*Set retains unique values.
print(s) # prints the set.
# s1 = s.union({1,2,3}) # Makes a new set.
# print(s,s1) # Prints both the sets.
s1 = s.intersection({1,2,3}) # Compares both the sets and gives the same values.
print(s,s1)
print(len(s)) # Prints hte length of the set.
print(min(s)) # Prints the minimum value in the set.
print(max(s)) # Prints the maximum value in the set.
print(s.isdisjoint(s1)) # Prints if the sets are disjoint.*True or False.
s.remove(2) # Removes the value () from the set.
