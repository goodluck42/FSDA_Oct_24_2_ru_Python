# a = 10
#
# def change():
#     global a
#
#     a = 42 # global
#
#
# change()
#
# print(a)

###################

# def foo(my_list): # 0xfa
#     # print(id(my_list))
#     my_list.append(10) # 0xfa
#     # print(id(my_list))
#     my_list.append(20) # 0xfa
#     # print(id(my_list))
#     my_list.append(30) # 0xfa
#     # print(id(my_list))
#
# def bar(my_str): # 0x20
#     # print(id(my_str))
#     my_str += "+" # 0x21
#     # print(id(my_str))
#     my_str += "-" # 0x22
#     # print(id(my_str))
#     my_str += "*" # 0x23
#     # print(id(my_str))
#     my_str += "/" # 0x24
#
#     return my_str
#
# list1 = [] # 0xfa
# str1 = "<empty-string>" # 0x20
# tuple1 = (1, "42", True)
#
# foo(list1)
# str1 = bar(str1) # 0x24
#
# print(list1)
# print(str1)

# mutable: list
# immutable: int, float, bool, tuple, str

# scope

# def print_is_positive(a):
#     if a > 0:
#         result = "positive"  # global
#     elif a < 0:
#         result = "negative"  # global
#
#     print(result)


