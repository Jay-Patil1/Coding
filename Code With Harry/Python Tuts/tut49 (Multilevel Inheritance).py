# MULTILEVEL INHERITANCE
class Dad:
    basketball = 1

class Son(Dad): # This takes the properties of ().
    dance = 1
    basketball = 6
    def isdance(self):
        return f"Yes I dance {self.dance} no if tomes."

class GrandSon(Son): # This takes the properties of ().
    dance = 6
    guitar = 1

    # def isdance(self): # This means the previous one gets ignored. If this is not edited the one above is considered.
    #     return f"Yes I dance very awesomely {self.dance} no of times."

darry = Dad()
larry = Son()
harry = GrandSon()

print(harry.isdance())
print(harry.basketball) # This is returned as it is inherited from further. This prints 6 as it finds it in the first place adn doesnt need to go further.

#Electronic Device.
#Pocket Gadget.
#Phone.