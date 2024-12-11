from random import randint

numbers = []
i = 0
count = int(input("Enter a number: ")) # 10

while i < count:
    i += 1

    rnd = randint(10, 49)

    numbers.append(rnd)

print(numbers)

i = 0

sum_result = 0

while i < len(numbers):
    sum_result += numbers[i]

    i += 1

print(sum_result)

# Найдите сумму элементов в списке из случайных чисел.

# В списке из случайных чисел, умножьте (в списке) все чётные числа на 2

# Сумму элементов, находящихся между первым
# и последним положительными элементами;
# [-10, 20, -30, 40, 11, 12, -70, -80]
#       ^       +   +    ^