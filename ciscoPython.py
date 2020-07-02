

def funct1():
    print("hello there!!")


def funct2(a, b):
    print(a + b)
    print(a / b)
    print(a * b)
    print(a - b)

class Person:
    def __init__(self, name, age, nation):
        self.name = name
        self.age = age
        self.nation = nation
    # creates instance of class
p1 = Person("Henrik", 22, "Latvian")

class Pizza:
    def __init__(self, pizza, type):
        self.pizza = pizza
        self.type = type

myPizza = Pizza("Margherita", "Deep Dish")


i = 10
while i == 10:
#code is running within the while loop
    name = input("what is your name: ")

    if name == "henrik":
        funct1()
        print("here are your details " + name + ": ")


        print(p1.name)
        print(p1.age)
        print(p1.nation)

    if name != "henrik":
        print("you are not henrik")
        funct2(2, 4)
        ## for loop
        for y in range(1, 10):
            print("hello there!!!!")


