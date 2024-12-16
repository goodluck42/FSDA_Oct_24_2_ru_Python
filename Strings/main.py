# mylist = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0],
# ]
#
# for item in mylist:
#     if mylist.count(item) == 1:
#         print("unique: ", item)

mylist = ["alpha", "beta", "gamma"]
mylist2 = ["zeta", "lambda"]

# mylist.remove("beta")
# mylist.pop(2)
# mylist.insert(0, "octa")
# mylist[0] = "tetra"
# mylist3 = mylist + mylist2
# mylist.reverse()
# mylist.extend(mylist2)

# print(mylist)
#
# mylist = [1, 2, 10, 4, 5]
#
# mymax = mylist[0] # 10
#
# for item in mylist:
#     if item > mymax:
#         mymax = item
#
# print(mymax)

name = "nazir"
surname = "Nabiev"

fullname = name + " " + surname

print(fullname)
print(fullname.count("Na"))
print(fullname.index("b"))
print(fullname.index("Nabiev"))

#########################

uppercase_name = name.upper()
lowercase_name = name.lower()

print(name)
print(uppercase_name)
print(lowercase_name)

# "сЛоВо".lower() == "слово"

if name.islower(): # isupper
    print("is lower")
else:
    print("is not lower")


##############

text = "Helloy, Nazir"

if text.isascii():
    print("is ascii")
else:
    print("is not ascii")

if text.isalpha():
    print("is alpha")
else:
    print("is not alpha")


sometext = "Hi42"

if sometext.isalnum():
    print("is alnum")
else:
    print("is not alnum")

number1 = "41"

if number1.isdigit():
    print("is digit")
else:
    print("is not digit")

number2 = "20.1"

if number2.isnumeric():
    print("is numeric")
else:
    print("is not numeric")



text = "hello how are you doing"

# text[0] = 'H'

text = text.replace("hello", "Nazir,")

if "how" in text:
    print("'how' is in the text")

print(text)

# result = text.split(" ")
#
# print(result[0])
#
# print(result)
# print(len(result))
#
# joined = "|||".join(result)
#
#
#
# print(joined)
#
# words = ["one", "two", "three"]
#
# joined2 = " ".join(words)
#
# print(joined2)
