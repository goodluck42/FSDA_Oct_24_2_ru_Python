# i = 0
#
# while i < 50:
#     print(i)
#     i += 1
#
#     if i == 9:
#         i += 1
#         continue
#
#     if i >= 10:
#         break
from turtledemo.penrose import start

# a = 0
#
# while a < 5:
#     if a == 3:
#         a += 1
#         continue
#
#     print(a)
#     a += 1

my_range = range(3, 7) # 3, 4, 5, 6
my_range2 = range(5) # 0, 1, 2, 3, 4
my_range3 = range(1, 10, 2) # 1, 3, 5, 7, 9

# print(list(my_range))
# print(list(my_range2))
# print(list(my_range3))

# for value in my_range2:
#     if value == 2:
#         break
#     print(value)

# print("done")

print("---------------")

for i in range(3):
    for j in range(3):
        if j == 1:
            print("  ", end='')
            continue
        print("* ", end='')
    print()

print("---------------")


# a = 0
# while a < 10:
#     if a == 5:
#         a += 1
#         continue
#
#     print(a)
#     a += 1




