# EXERCISE 11
# Email collector.

                    # SOLUTION

'''
Author: Jay Patil
Purpose: Learning Python
'''                    

import re


str = '''
patiljay32145@gmail.com, 9405678249,
yashpatil@gmail.com, 8624968607,
pajitkumar@yahoo.com, 9850833066,
'''
email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+", str)
email1 = re.findall(r"\w+@\S+\w", str)
email2 = re.findall(r"[A-Za-z0-9]+@[a-zA-Z0-9]+[.][a-zA-Z0-9]+",str)
print(email)
print(email1)
print(email2)
