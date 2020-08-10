# USING ELSE WITH FOR LOOP
# When the for loop normally ends then else can be used with it.
#  For Loop ends by 2 ways-
# 1] When the iterable is over.
# 2] When given a break statement.
khana = ["roti", "sabzi", "chawal"]

for item in khana:
    print(item)
else:
    print("This for loop ended normally.")
# Here else is used with the for loop.


for item in khana:
    if item == "paratha":
        break
else:
    print("Your item is not in the list.")
# If the given value is not in the list then the else is run.


for item in khana:
    if item == "roti":
        break
else:
    print("Your item is not in the list.")
# If the given item is in the list then the else is not run.
