# ---------------------------------------------------------------------------------------------

# 1. We’ve already implemented optional parameters 
# in pervious practical (Practical 2). 
# Now try to pass the only 2nd optional parameter to the 
# function by referring its name.

def SayHello(greeting = "Hello", name = "User"):
    return greeting + ", " + name + "!"

print(SayHello(name = "Ritwick")) # Output : Hello, Ritwick!
print(SayHello(name = "Ritwick", greeting = "Hiii")) # Output : Hiii, Ritwick!

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

# 2. Try print(“Python”, “is”, “awesome”). Check what the output you get.
# Now modify the output like this - “Python-is-awesome!” 

print("Python", "is", "awesome") # Output: Python is awesome
print("Python", "is", "awesome", sep = "-", end="!") # Output: Python-is-awesome!

# ---------------------------------------------------------------------------------------------