# PICKLE MODULE
import pickle
# Store-able thing.
# Pickling is preserving.

# Pcikling a python object.
cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tzuki"]
file = "mycar.pkl"
fileobj = open(file, "wb")
pickle.dump(cars, fileobj)  # This takes file object not a file.
fileobj.close()

# De-Pickling
file = "mycar.pkl"
fileboj = open(file ,'rb')
mycars = pickle.load(fileboj)
print(mycars)
print(type(mycars))
# pickle.loads = ?
