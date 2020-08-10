# BREAK AND CONTINUE STATEMENTS
# i = 0
# while(True):
#     if i+1<5:
#         i = i + 1
#         continue # Move back to the while true loop
#     print(i+1, end=" ")
#     if(i==44):
#         i = i + 1
#         break # Stop the loop.
#     i = i + 1

# QUIZ
# it will continue till one prints No. less than 100. if it becomes more tham 100.

while(1):
    inp = int(input("Enter a number\n"))
    if inp>100:
        print("Congrats!!\n")
        break
    else:
        print("Try Again\n")
        continue

