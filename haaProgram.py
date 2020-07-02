##name = input("enter in your name: ")

#print("Hello, " + name)

#age = int (input(name + ", what is your age: "))

#year = str ((2019 - age) + 100)

#print(name + " will be 100 years old in the year " + year)


class Pizza:

    def __init__(self, pizzaName, topping, type):
        self.pizzaName = pizzaName
        self.topping = topping
        self.type = type



def my_function():
    print("taking in the customer's order")
    print("constructing the pizza")
    print("now baking the pizza in the oven")
    print("your order is now complete, thank you!")

def price():
    t = 5
    p = 10
    type = 7
    print(t + p + type)

count = 0

## allows for continous input into the program without reopening it each time
while(count < 9):



    pizzaName = input("enter in the pizza you want to order: ")
    pizzaTopping = input("what topping would you like: ")
    pizzaType = input("which pizza type: ")


## inputted data takes place of variables in Pizza class
    pizza = Pizza(pizzaName, pizzaTopping, pizzaType)

##prints out inputted data to user
    my_function()
    price()

    print(pizza.pizzaName + " pizza topped with " + pizza.topping)




