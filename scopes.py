# In python global is anything that can be accessed by all parts of a program
# Scopes are separated by spaces.


myInteger = 56
my_boolean = False

def space(): 
    global myInnerInteger, my_inner_boolean
    myInnerInteger = 2
    my_inner_boolean = True

    print(
        type(myInteger),
        type(my_boolean)
    )

space()  
 
print(myInnerInteger, my_inner_boolean)
print(myInteger, my_boolean)


# CLASSWORK 2 (15LPs)
# 1. Create a function called store_name, inside the function create a global variable called name and assign it a name. (9LPs)
# 2. Print the global variable outside the function. (6LPs)

def store_name():
    global animal
    animal = "penguin" 

store_name()
print(animal)

