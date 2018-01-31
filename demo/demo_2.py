# ---------------------------------------------------------------------------------------------

# demo of optional parameter

def IncrementValue(num, incrementBy = 1):
    return num + incrementBy

print(IncrementValue(55)) #Output : 56
print(IncrementValue(55, 5)) #Output : 60

# ---------------------------------------------------------------------------------------------