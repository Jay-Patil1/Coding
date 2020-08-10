# EXERCISE 2
# FAULTY CALCULATOR
# 45*3=555,56/9=4,56+9=77

'''
Author: Jay Patil
Purpose: Learning Python
'''

                    # SOLUTION

No1 = int(input("Enter the first No."))
op = (input("Enter the operation"))
No2 = int(input("Enter the second No."))

if op=="*":
    if No1==45 and No2==3 or No1==3 and No2==45:
        print(555)
    else:
        print(No1*No2)

elif op=="/":
    if No1==56 and No2==9 :
        print(4)
    else:
        print(No1/No2)

elif op=="+":
    if No1==56 and No2==9 or No1==9 and No2==56:
        print(77)
    else:
        print(No1+No2)
        