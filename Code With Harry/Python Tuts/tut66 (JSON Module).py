# JSON MODULE
# JSON = Java Script Object Notation.
import json

data = '{"var1":"Harry", "var2":56}'
# print(data["var1"])  # This cannot be used without parsing.

parsed = json.loads(data)  # This parses the data.
# print(parsed["var1"])
print(type(parsed))  # The data is converted into a dictionary.



data2 = {
    "Channel_name":"CodeWithHarry",
    "Cars":['bmw', 'audie a8', 'ferrari'],
    "fridge":('roti',540),
    "isbad":False
}

jscomp = json.dumps(data2)
print(jscomp)

# Task1 - json.load?
# Task2 - What is sort_keys parameter in dumps?
