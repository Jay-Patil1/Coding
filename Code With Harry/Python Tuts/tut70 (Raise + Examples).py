# RAISE + EXAMPLES
# a = input("What is your name?\n")
# b = input("How much do you earn?")
# if int(b) == 0:
#     raise ZeroDivisionError("Your sallery is 0.")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed.")
#
# print(f"Hello {a}")
# # 1000 lines taking 1 hour.


                    # In Try Except.
c = input("Enter your name.")
try:
    print(a)
except Exception as e:
    if c=="harry":
        raise ValueError("Harry is blocked.")
    print("Exception handeled")
