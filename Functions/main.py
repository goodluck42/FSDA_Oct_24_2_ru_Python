# # a = 42 # global variable
# # b = 13 # global variable
#
# def is_negative(num):
#     if num < 0:
#         return True
#     else:
#         return False
#
#
# def my_sum(num1, num2, num3): # parameters
#     result = num1 + num2 + num3
#
#     return result
#
#
# # res1 = my_sum(20, 10, 30) # arguments
# # res2 = my_sum(40, 50, 60) # arguments
# #
# # print(res1)
# # print(res2)
# #
# # print("Bye-bye!")
#
#
# res = is_negative(5)
#
# print(res)
#
#
# #################
# # def print_menu():
# #     print("1. Sign up") # Registration
# #     print("2. Sign in") # Login
# #     print("3. Add book")
# #     print("4. Remove book")
# #     print("5. Print books")
# #     print("6. Exit")
# #
# #
# # while True:
# #     print_menu()
# #
# #     choice = input()
# #
# #     if not choice.isdecimal():
# #         print("You are an idiot!")
# #         continue
# #
# #     if choice == "1":
#



# Task 1
# Создать функцию MyPow для возведения числа в степень
# (положительные и отрицательные и учесть нулевую степень числа).
# Без **
# Task 2
# Создать функцию для вывода на экран пирамиду из * в столько строк,
# сколько введёт пользовать. Например (3) :
#   *
#  * *
# * * *
#
# Task 3
# В функции есть 2 вложенных цикла while True. Остановите оба цикла и завершите работу функции.

#
# Task 4
# Создать функцию, которая проверяет, является ли переданная строка палиндромом.
#
# Запрещено использовать [::-1], преобразования, reverse.
# Task 5
# Напишите функцию, которая принимает лист и делает его реверс.
# (без использования метода .reverse, [::-1] и преобразований).


## BAD
# def sum(a, b):
#     res = a + b
#     print(res)
#
#     print(res * 2)

## GOOD
# def sum(a, b):
#     return a + b

# res = sum(10, 20)
#
# print(res * 2)