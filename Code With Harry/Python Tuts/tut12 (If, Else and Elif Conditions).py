# IF ELSE AND ELIF CONDITIONS
var1 = 6
var2 = 56
print("Type your No.")
var3 = int(input())
# If else is used for the following.
if var3>var2:  # To go into the statement use :.*Indentation.
    print("Greater")
if var3==var2:# Double == is used because single = is an assignment operator.
    print("Equal")
else:
    print("Lesser")

# IF if function is used all the catagories are checked.
# After using elif , if the if function is true then elif is skipped. And if if is false the elfi is checked.
if var3>var2:
    print("Greater")
elif var2==var3:
    print("Equal")          # This is an if,else ladder.
else:
    print("Lesser")


list1 = [5,7,3]
print(5 in list1) # Prints whether the value is in the list.*True or False.
if 5 in list1:
    print("Yes it is in the list")
print(15 not in list1) # Prints whether the value is not in the list.*True or False.
if 15 not in list1:
    print("No its not in the list")

#QUIZ
print("What is your age?")
age = int(input())
if age<18:
    print("You cannot drive.")
elif age>18:
    print("You can drive.")
elif age==18:
    print("We cant state whether you can drive or not")
