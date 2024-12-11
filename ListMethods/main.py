# mylist = [10, 20]
# mytuple = (10, "str")
#
# print(mytuple[0])
# print(mytuple[1])
from random import randint

#############

# CRUD - CREATE READ UPDATE DELETE

names = []

print("1. Add name")
print("1.1 Insert name")
print("2. Remove name")
print("2.1 Remove name by index")
print("3. Print name by index")
print("4. Change name by index")
print("P. Print index by name")
print("5. Print names")
print("S. Sort names")
print("C. Count names")
print("6. Exit")

while True:
    action = input()

    if action == "1":
        name = input("Enter a name: ")

        names.append(name)
    elif action == "1.1":
        index = int(input("Enter index: "))
        name = input("Enter a name: ")

        names.insert(index, name)
    elif action == "2":
        name = input("Enter a name: ")

        if name in names:
            names.remove(name)
    elif action == "2.1":
        index = int(input("Enter index: "))

        names.pop(index)
    elif action == "3":
        index = int(input("Enter index: "))

        print(names[index])
    elif action == "4":
        index = int(input("Enter index: "))
        name = input("Enter a name: ")

        names[index] = name
    elif action == "P":
        name = input("Enter a name: ")

        name_index = names.index(name)
        print(name_index)
    elif action == "5":
        for name in names:
            print(name)
    elif action == "S":
        names.sort()
    elif action == "C":
        name = input("Enter a name: ")

        cnt = names.count(name)

        print(cnt)
    elif action == "6":
        break


numbers = [randint(0, 100) for x in range(10)]

for item in numbers:
    print(item)

num = int(input("Enter a number: "))

if num in numbers:
    print("Exists")
else:
    print("Not Exists")

#  0      1      2      3
# [Nazir, Tural, Revan, Maqsud]

mylist = [4, 5, 10, 12, 16]

i = 0

while i < len(mylist):
    print(mylist[i])

    i += 1

print("#########################")
for item in mylist:
    print(item)

print("#########################")
for i in range(len(mylist)):
    print("index: ", i)
    print("element: ", mylist[i])

