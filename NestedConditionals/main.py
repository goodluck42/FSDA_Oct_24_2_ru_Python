# >, <, >=, <=, ==, !=

# x = int(input())

# if x % 2 == 0:
#     print("even")
# else:
#     print("odd")

# number = int(input("Enter a number: "))
#
# if number < 0:
#     print("negative")
# elif number > 0:
#     print("positive")
# else:
#     print("zero")

print("1. New game")
print("2. Load game")
print("3. Multiplayer")
print("4. Settings")
print("5. Exit")

option = int(input("Enter your choice: "))

if option == 1:
    print("New game started...")
elif option == 2:
    save_num = int(input("Enter your save number: "))

    if save_num == 1:
        print("Loading first save...")
    elif save_num == 2:
        print("Loading second save...")
    elif save_num == 3:
        print("Loading third save...")
    else:
        print("Save does not exist")
elif option == 3:
    print("Multiplayer session started...")
elif option == 4:
    print("Entering settings")
elif option == 5:
    print("Exiting...")
else:
    print("Incorrect input")



num = int(input())

if num > 0:
    if num % 2 == 0:
        print("positive even")
    else:
        print("positive odd")
else:
    if num % 2 == 0:
        print("negative even")
    else:
        print("negative odd")



a = 42
b = 42.0
c = "my text"
d = False

a = 20
# a is between 20 and 50

if 20 < a < 50:
    pass