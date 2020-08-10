# TIME MODULE
# How to find the execution time of a program?
import time

initial = time.time()# This gives number of ticks.That is number of seconds.
print(initial)
k = 0
while(k<45):
    print("This is Jay")
    time.sleep(2) # The programm stops for () ticks.
    k+=1
print("While loop ran in",time.time() - initial,"Seconds")

initial2 = time.time()
for i in range(45): # Prints () for 45 times
    print("This is Jay")
print("For loop ran in",time.time() - initial2,"Seconds")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime) # This gives us the current time.
# asc time converts it into readable form.

            # Learn about time module from time module.