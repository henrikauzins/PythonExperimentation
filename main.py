import random

def randomFunction():
    arr = [2,6,7,9,8]
    arr_length = len(arr)

    for i in range(0, 1):
        print("random function")
    ## gets length of arr through for loop and prints out the array
    for x in range(arr_length):
        print(arr[x])

def HFunction():
    num2 = random.randint(1, 20)
    while num2 < 10:
        print("less than 10")
        break
        if num2 > 10:
            print("more than 10")
            break


class Student:
    def __init__(self, name, nation, course, year):
        self.name = name
        self.nation = nation
        self.course = course
        self.year = year

student_block = []

#variables

num = random.randint(2, 10)
print(HFunction())
print(num)
print(randomFunction())
name = input("what is your name: ")
nation = input("what is your nation: ")
course = input("what course do you study: ")
year = input("what school year are you in: ")

new_student = Student(name, nation, course, year)
student_block.append(name)
student_block.append(nation)
student_block.append(course)
student_block.append(year)

print("Student Summary")
print(student_block)
while True:
    print("what course did you study at university? ")
    if course == "computer science":
        print("001110111")
        print("what a nerd")
        break

    else:

        print("you all good lol")
        break

