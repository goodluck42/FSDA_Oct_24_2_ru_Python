# arithmetical ops: +, -, *, /, **, //, %
# assigment ops: =
# shorthand ops: +=, -=, *=, /=, **=, //=, %=
# comparison ops: >, <, >=, <=, ==, !=
# logical ops: not, and, or
###############################
# a = 2
#
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")
#
# if a == 2:
#     print("is 2")
# elif 1 == a:
#     print("is 1")
#
#
# # literals
#
# l1 = 42.13
# l2 = 3
# l3 = False
# l4 = "32"
# l5 = int(input()) # not a literal

a = ""

print(bool(a))  # explicit typecast (str to bool)

# implicit typecasts
# if "": # str -> bool (False)
#     print("1")
# elif 100: # int -> bool (True)
#     print("2")

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("even positive")

if num > 0 or num % 2 == 0:
    print("even or positive")


# or
# 1 or 1 => 1
# 1 or 0 => 1
# 0 or 1 => 1
# 0 or 0 => 0

# and
# 1 and 1 => 1
# 1 and 0 => 0
# 0 and 1 => 0
# 0 and 0 => 0

# not
# not 1 => 0
# not 0 => 1

# 1 and 0 or 1 and 1


a = 5

if a >= 1 and a <= 10:
    print("in range")