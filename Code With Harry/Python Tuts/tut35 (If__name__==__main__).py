# IF __NAME__==__MAIN__
import sklearn
def printjay(string):
    return (f"Give this string to me. {string}")

def add(num1, num2):
    return num1 + num2 + 5



print("and the name is", __name__) # The name is main as it is run in the main file.
if __name__ == '__main__': # The following program will only be executed in the main file. And not where the file is imported.
    print(printjay("JAY"))
    o = add(4, 6)
    print(o)