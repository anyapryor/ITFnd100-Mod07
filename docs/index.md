# Pickling
Binary data and Pickling
 Import allows you to access other files that were previously created. Binary format allows you to both obscure the data and to make it smaller so it may be easier to use. Pickling is called by importing first, as the commands to pickle data are not inherent in Python. By pickling we take data and transform the format to binary and create it as a reference object, so that it will persist in the file and format we create. Pickling uses either the dump or read commands, dump to put data into binary format and read to transform it back into a human readable format.

Here is the lab for pickling:

```
# ------------------------------------------------- Z
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# <YourName>,<1.1.2030>,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "ab")
    pickle.dump(list_of_data, objFile)
    objFile.close()
def read_data_from_file(file_name):
    objFile = open(file_name, "rb")
    list_of_data = pickle.load(objFile)  # load() only loads one row of data.
    objFile.close()
    return list_of_data
# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
stridvalue = str(input("Enter an ID:"))
strnamevalue = str(input("Enter a Name: "))
lstCustomer= [stridvalue,strnamevalue]
# TODO: store the list object into a binary file
save_data_to_file(strFileName,lstCustomer)
# TODO: Read the data from the file into a new list object and display the contents
print(read_data_from_file(strFileName))
```
The data put into the file using the pickle.load function keeps it the same as it originally was created, regardless of the input data gathered from the input block.
I found this video interesting as it used a string variation for the load and dump functions, and it also created a class.

```#from https://www.youtube.com/watch?v=XzkhtWYYojg

import pickle
#pickle.dump() #this works with a file type object
#pickle.dumps() #this works with a string type object
#pickle.load() #this works with a file type object
#pickle.loads() #this works with a string type object

class example_class: #create a class with a variety of data types
    a_number=25
    a_string="gotcha"
    a_list=[1,2,3]
    a_dictionary={"first":42, "second": "Sam I am","third":[3,4,5]}
    a_tuple=(88,44)

my_object=example_class()
my_pickled_object=pickle.dumps(my_object)
print(f"This is my pickled object:\n{my_pickled_object}\n") #shows the object in bianary format
#now we test to see if we can change the pickled object by redefining one of the members of the class
my_object.a_dictionary=None
#unpickle and show the item we tried to change
my_unpickled_object=pickle.loads(my_pickled_object)
print(
    f"a_dictionary of unpickled object:\n{my_unpickled_object.a_dictionary}\n")
```
I also found the example in the book interesting as it used a shelve function to act like a dictionary for the pickled object:
```
# Pickle It
# Demonstrates pickling and shelving data
# from Python Programming for the Absolute Beginner by Michael Dawson, p.200
import pickle, shelve

print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
f = open("pickles1.dat", "wb") #wb=write bianary
pickle.dump(variety, f) #put list  variety into file f
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nUnpickling lists.")
f = open("pickles1.dat", "rb") #rb= read binary
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

print("\nShelving lists.")
s = shelve.open("pickles2.dat") #shelve creates a dictionary like object but is more memory efficient
s["variety"] = ["sweet", "hot", "dill"] #create a key and assigns values to it, here variety is the key
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]
s.sync()    # make sure data is written

print("\nRetrieving lists from a shelved file:")
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])
s.close()

input("\n\nPress the enter key to exit.")
```
This site has a good summary on pickling:  https://www.geeksforgeeks.org/understanding-python-pickling-example/
