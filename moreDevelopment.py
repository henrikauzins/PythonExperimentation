import random

name = input("enter in your name: ")

arr = ["hello there", "sveiki", "privet"]
arr1 = ["off you pop", "go away", "ej prom"]


if name == "henrik" or "Henrik":
    print(random.choice(arr))

else:
    print(random.choice(arr1))

## for loop
for y in range(2,10):
    print(y)


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # swaps elements found if it is greater
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [2,10,-1,9,99,8]

bubbleSort(arr)

print("sorted array:")

for i in range(len(arr)):
    print("%d" %arr[i]),
