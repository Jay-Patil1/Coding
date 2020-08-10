# ENUMERATE FUNCTION
l1 = ["Bhindi", "Aloo", "Chopsticks", "Chowmein" ]

# i = 1
# for item in l1:
#     if i % 2 != 0:
#         print(f"Jarvis please buy {item}")
#     i += 1


                # Enumerate Function.

for index, item in enumerate(l1):
    if index%2==0: # If index is 0 therefore it is 0.
        print(f"Jarvis please buy {item}")
