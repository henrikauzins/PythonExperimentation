class TestClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def TestFunction(abc):

        print("My name is " + abc.name)

def myFunct():
    x = 5
    print(x)

t1 = TestClass("Henrik", 22)
print(t1)
t1.TestFunction()

myFunct()