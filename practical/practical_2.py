# ---------------------------------------------------------------------------------------------

# 1. Lets modify the last task SayHello(“Hi”, “Akash”) function 
# and make the two parameter of function as optional parameter. 

def SayHello(greeting = "Hello", name = "User"):
    return greeting + ", " + name + "!"


print(SayHello()) # Output : Hello, User!
print(SayHello("Hey", "Ritwick")) # Output : Hey, Ritwick!


# ---------------------------------------------------------------------------------------------