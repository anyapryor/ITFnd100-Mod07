#-----------------------------------#
# Title: Pickling and Error Handling
# Developer: Anya Pryor
# Change Log: Combined exercises here 11/29/21
#-----------------------------------#

#Pickling demo
#from https://www.youtube.com/watch?v=XzkhtWYYojg

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

#try/ except error handling
# Handle It
# Demonstrates handling exceptions
# From Python for Absolute Beginners by Michael Dawson p.206

# try/except
try:
    num = float(input("Enter a number: "))
except:
    print("Something went wrong!")

# specifying exception type
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")

# handle multiple exception types
print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Something went wrong!")

print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("I can only convert a string or a number!")
    except ValueError:
        print("I can only convert a string of digits!")

# get an exception's argument
try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
    print("That was not a number! Or as Python would say...")
    print(e)

# try/except/else
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered the number", num)

input("\n\nPress the enter key to exit.")
