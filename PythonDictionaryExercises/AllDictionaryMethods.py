a = {1: "first name", 2: "last name", "age": 33}
# print(a.keys())  # it will print all keys as a list
# print(a.values())  # it will print all values as a list
# print(a.items())
# b = a.items()  # A view object that displays a list of a given dictionary’s (key, value) tuple pair.
# print(a.pop('age'))  # o/p - 33
# print(a.get(2))
# print(a.popitem()) # Pops the last key-value pair

for i in a:
    print(i, " : ", a[i])

print(a.values())
print(a.keys())



