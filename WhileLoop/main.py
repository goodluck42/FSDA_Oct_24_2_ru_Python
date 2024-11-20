# not, and & or

# 1 or 0 and 0


# 1 or 1 => 1
# 1 or 0 => 1
# 0 or 1 => 1
# 0 or 0 => 0

# and
# 1 and 1 => 1
# 1 and 0 => 0
# 0 and 1 => 0
# 0 and 0 => 0

# (1 or 0) and 1

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
#
# if b == 0:
#     print("Cannot divide by zero")
# else:
#     if a > 100 and b > 100:
#         print(a / b)
#     else:
#         print("An error")



print("----descending----")

a = 3

while a >= 0:
    print(a)
    a -= 1 # decrement

print("----ascending----")

b = 0
while b <= 3:
    print(b)
    b += 1 # increment

print("----Goodbye----")