'''
Author: Jay Patil
Purpose: Learning Python
'''

class ElectronicDevice:
    def __init__(self, name, price, working):
        self.name = name
        self.price = price
        self.working = working


class PocketGadget(ElectronicDevice):
    def __init__(self, names, pricea, use):
        self.pricea = pricea
        self.names = names
        self.use = use


class Phone(PocketGadget):
    def __init__(self, brand, cost, feature):
        self.brand = brand
        self.cost = cost
        self.feature = feature


Realme = Phone("Realmi", 15000, "Great battery life.")
HeadPhones = PocketGadget(f"Air Pods", 14999, "Listen to music")
Phone = ElectronicDevice("IPhone", 26000, "")
