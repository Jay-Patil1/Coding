# *ARGS AND **KWARGS
# args and kwargs are optional.They can be named as anything.
def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)
def funargs(normal ,*argsrohan, **kwargsbala): # If the arguement is used later its an error.Then use args and then kwargs
    print(normal)
    for item in argsrohan:
        print(item)
    print("Now i would like to introduce some of our heroes.")
    for key,value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Jay", "Yash", "Shivam")

har = ["Harry", "Rohan", "Jay", "Yash", "Hammad", "The programmer"]
normal = "I am a normal Arguement"
kw = {"Rohan":"Monitor", "Harry":"Fitness Trainer",
      "Shivam":"Cook","Jay":"coordinator"}
funargs(normal,*har,**kw) # The star is compulsory.
# If the list is updated the args also get updated.



