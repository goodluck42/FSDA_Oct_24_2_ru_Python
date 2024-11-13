## str to int
# var = input()
# int_value = int(var) # <-- explicit typecast
#
# print(int_value * 2)

## str to float
# var2 = input()
# float_value = float(var2)
#
# print(float_value / 2)

## float to int

# fvalue = float(input()) # <- typecast
# typecast_result = int(fvalue) # <- typecast
#
# print(typecast_result)

## int to float

# ivalue = int(input()) # <- typecast
# typecast_result = float(ivalue) # <- typecast
#
# print(typecast_result)

## int & float to str

# value = float(input())
#
# typecast = str(value)
#
# print(typecast * 2)

## int, float, str to bool

# value = ""
# typecast = bool(value)
#
# print(typecast)

## implicit typecasts
# value = 42
# value2 = 42.13
# value3 = "hello python"
# value4 = True
#
# print(value, value2, value3, value4)

a = 10
b = 3
# int to float

result = a / b

print(result)
print(type(result))
######
a1 = 10.3
b1 = 3.3

result = a1 // b1

print(result)
print(type(result))
######

a2 = 10
b2 = 0.5

result = a2 + b2

print(result)