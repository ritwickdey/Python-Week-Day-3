# Demo of Local & Global Variable

num1 = 10 # global varibale
num2 = 20 # global varibale

def fun():
    global num1 # refering num1 as global varibale
    num1 = 5 # Global variable updated
    num2 = 6 # Wait, it's not updating global varibale, it's creating new local variable
    num3 = 7 # Local variable
    print("From local scope: num1, num2, num3 = ", num1, num2, num3)


fun()
print("From Global scope: num1, num2 = ", num1, num2)
# 'num3' is no more available as it's a local varibale of 'fun()'


