# EXERCISE 5
# Health Management System
# 3 clients = Harry, Rohan and Hammad
def getdate():
    import datetime
    return datetime.datetime.now()
# Total 6 files
# write a function that when executed takes input client name.
# (time) What did he eat/do
# to retrieve exercise or food for any client.

                    # SOLUTION

'''
Author: Jay Patil
Purpose: Learning Python
'''

def take(k):

    if k==1:
        c = int(input("Enter 1 for Exercise and 2 for Food: \n"))
        if c==1:
            value = input("Enter Exercise:\n")
            with open("HarryE.txt","a") as HE:
                HE.write(str(getdate())+":"+ value +"\n")
            print(value + " Saved")
        elif c==2:
            value = input("Enter Food:\n")
            with open("HarryF.txt","a") as HF:
                HF.write(str(getdate())+":"+ value +"\n")
            print(value + " Saved")

    elif(k==2):
        c = int(input("Enter 1 for Exercise and 2 for Food: \n"))
        if c==1:
            value = input("Enter Exercise:\n")
            with open("RohanE.txt","a") as RE:
                RE.write(str(getdate())+":"+ value + "\n")
            print(value + " Saved")
        elif c==2:
            value = input("Enter Food:\n")
            with open("RohanF.txt","a") as RF:
                 RF.write(str(getdate())+":"+value+"\n")
            print(value+" Saved")

    elif(k==3):
        c = int(input("Enter 1 for Exercise and 2 for Food: \n"))
        if c==1:
            value = input("Enter Exercise:\n")
            with open("HamadE.txt","a") as HAE:
                HAE.write(str(getdate())+":"+ value + "\n")
            print(value + " Saved")
        elif c==2:
            value = input("Enter Food:\n")
            with open("HamadF.txt","a") as HAF:
                 HAF.write(str(getdate())+":"+value+"\n")
            print(value+" Saved")
    else:
        print("Enter valid data[ (1 for Harry) , (2 for Rohan) , (3 for Hamad) ]")

def retrive(k):
    if k==1:
        c = int(input("Enter 1 for Exercise and 2 for Food: \n"))
        if c==1:
            with open("HarryE.txt") as RHE:
                for i in RHE:
                    print(i,end="")
        elif c==2:
            with open("HarryF.txt") as RHF:
                for i in RHF:
                    print(i,end="")

    elif k==2:
        c = int(input("Enter 1 for Exercise and 2 for Food: \n"))
        if c==1:
            with open("RohanE.txt") as RRE:
                for i in RRE:
                    print(i,end="")
        elif c==2:
            with open("RohanF.txt") as RRF:
                for i in RRF:
                    print(i,end="")

    elif k==3:
        c = int(input("Enter 1 for Exercise and 2 for Food: \n"))
        if c==1:
            with open("HamadE.txt") as RHAE:
                for i in RHAE:
                    print(i,end="")
        elif c==2:
            with open("HamadF.txt") as RHAF:
                for i in RHAF:
                    print(i,end="")
    else:
        print("Enter valid data[ (1 for Harry) , (2 for Rohan) , (3 for Hamad) ]")

print("Exercise And Food Records")
a = int(input("Lock or Retrive Data?\n"
              "1 for Lock\n"
              "2 for Retrive\n"))
if a ==1:
    b = int(input("Enter Client Name:\n"
                  "1 for Harry\n"
                  "2 for Rohan\n"
                  "3 for Hamad\n"))
    take(b)
elif a ==2:
    b = int(input("Enter Client Name:\n"
                  "1 for Harry\n"
                  "2 for Rohan\n"
                  "3 for Hamad\n"))
    retrive(b)
