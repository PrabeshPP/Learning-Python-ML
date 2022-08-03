from unittest import result


def addFive(a):
    a+=5
    print(a)


addFive(20)

#Types of Functions
def greeting():
    print("Good Morning")

greeting()

def greet(name):
    print("HI "+name+"!")

greet("Prabesh")

def mul(x):
    return x*x

result=mul(5)
print(result)