# COMPREHENSIONS
            # List Comprehensions.
ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)
print(ls)
# This can be made in one line using the following loop.
ls = [i for i in range(100) if i%3==0]
print(ls)

            # Dictionary Comprehension.
dict1 = {i : f"item {i}" for i in range (1, 10001) if i%100==0}
dict1 = {i : f"item {i}" for i in range (5)}
dict2 = {value:key for key,value in dict1.items()}  # The key and the values are interchanged.
print(dict1,"\n",dict2)


            # Set Comprehension.
dresses = {dress for dress in ["dress1","dress2",
                               "dress1","dress2",
                               "dress1","dress2"]}
print(type(dresses))

            # Generator Comprehension.
evens = (i for i in range(100) if i%2==0)
print(evens.__next__())

for item in evens:
    print(item)

# QUESTION
# Take a user input.
# Ask for how many items to be added.
# Take input.
# Ask for type of comprehension.
# Make the comprehension and print.
