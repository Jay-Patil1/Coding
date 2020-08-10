# EXERCISE 10
# Pickling Iris
# UCI ml repository

            # SOLUTION

'''
Author: Jay Patil
Purpose: Learning Python
'''

import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(data)

l1 = data.split("\n")
# print(l1)

l2 = [item.split(",") for item in l1 if len(item)!=0]
print(l2)

with open("Myiris.pkl", "wb") as f:
    pickle.dump(l2, f)



# Use this to read this pickle file
# import pickle
# with open("Myiris.pkl", "rb") as f:
#     pickle.load(f)
