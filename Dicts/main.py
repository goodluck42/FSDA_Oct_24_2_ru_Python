# mutable: list, dict
# immutable: int, float, bool, str, tuple

# book = {
#     "author": "John",
#     "name": "Путешествие двоечников",
#     "genres": ["Horror", "Fantasy"],
#     "year": 2025
# }
#
# book["year"] = 2024
#
# book2 = {
#     "author": "John",
#     "name": "Путешествие двоечников 2",
#     "genres": ["Horror", "Fantasy"],
#     "year": 2025
# }

# book.pop("year")

# key = input("Enter a key: ")
# value = book.get(key)
# # value = book[key]
#
# if value is None:
#     print("Key does not exist")
# else:
#     print(value)
#
# book_k = book.keys()
#
# print(book_k)

# print(book[key])

# for key in book:
#     print(key)
#     print(book[key])


# print(book.items())

# for k, v in book.items():
#     print(k, v)

# books = []
#
# books.append(book)
# books.append(book2)
#
# # print(books[0]["genres"][1])
# print(books)
# while True:
#     name = input("Enter a book name: ")
#     author = input("Enter a book author: ")
#     # ...
#
#     books.append({
#         "name": name,
#         "author": author,
#         "genres": ["Horror", "Fantasy"],
#         "year": 2020
#     })


## write text
# f = open("data.txt", "w")
#
# f.write("Goodbye cruel world!")
# f.close()


## read text

# f = open("data.txt", "r")

# text = f.read()

## read lines
# line = f.readline()
# line2 = f.readline()

# print(line)
# print(line2)


## read all lines
# while True:
#     line = f.readline()
#
#     if line == "":
#         break
#
#     print(line)

# lines = f.readlines()
#
# print(lines)


## JavaScript Object Notation

import json
#
# book = {
#     "author": "John",
#     "name": "Путешествие двоечников",
#     "genres": ["Horror", "Fantasy"],
#     "year": 2025
# }
#
# file = open("books.json", "w")
# json = json.dumps(book)
#
# file.write(json)
# file.close()


file = open("books.json", "r")

json_data = file.read()

book = json.loads(json_data)

file.close()

print(book["author"])


