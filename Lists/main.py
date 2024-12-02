# range(1, 6) 1 2 3 4 5
# range(5) 0 1 2 3 4
# range(1, 10, 2) 1 3 5 7 9
import random

# for item in range(10):
#     print(item)

# str, float, int, bool

# a = 13
#
# if a % 2 == 0:
#     print("even")


# 0 -> 9
# i = 0
# while True:
#     print(i) # i = 0
#     i += 1 # i = 1
#     if i >= 9:
#         break

# i = 0
# while i < 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1


# lists
#          0   1   2   3   4
# numbers = [100, 200, 300, 420, 500]
#
# print(numbers[1] + numbers[2])
# numbers[0] = 5
# print(numbers)

# iteration using while loop

# i = 0
# while i < 5:
#     numbers[i] *= 0.9
#     i += 1
#
# print(numbers)

###############
# nums = []
#
# while True:
#     number = int(input("Enter a number: "))
#     nums.append(number)
#
#     if number == 0:
#         break
#
# print(nums)

from random import randint

nums = []

i = 0

while i < 10:
    rnd = randint(10, 99)
    i += 1

    nums.append(rnd)

print(nums)


i = 0

while i < 10:
    if nums[i] > 50:
        print(nums[i])

    i += 1

print("#################")
my_list = [1, 2, 3, 4, 5, 10]


i = 0
sum = 0
while i < 6:
    sum += my_list[i]

    i += 1

print(sum)


