# In python global is anything that can be accessed by all parts of a program
# Scopes are separated by spaces.


myScope = 56
my_boolean = False

def space(): 
    # global myScope, my_boolean
    myInnerScope = 2
    my_inner_boolean = True

    print(
        type(myScope),
        type(my_boolean)
    )
    print(myInnerScope, my_inner_boolean)
    
# print(myInnerScope, my_inner_boolean)
print(myScope, my_boolean)
space()

