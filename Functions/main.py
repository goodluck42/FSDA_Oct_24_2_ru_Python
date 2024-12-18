# a = 42 # global variable
# b = 13 # global variable

def is_negative(num):
    if num < 0:
        return True
    else:
        return False


def my_sum(num1, num2, num3): # parameters
    result = num1 + num2 + num3

    return result


# res1 = my_sum(20, 10, 30) # arguments
# res2 = my_sum(40, 50, 60) # arguments
#
# print(res1)
# print(res2)
#
# print("Bye-bye!")


res = is_negative(5)

print(res)


#################
# def print_menu():
#     print("1. Sign up") # Registration
#     print("2. Sign in") # Login
#     print("3. Add book")
#     print("4. Remove book")
#     print("5. Print books")
#     print("6. Exit")
#
#
# while True:
#     print_menu()
#
#     choice = input()
#
#     if not choice.isdecimal():
#         print("You are an idiot!")
#         continue
#
#     if choice == "1":

