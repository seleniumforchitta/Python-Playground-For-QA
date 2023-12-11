chit = ["Chittaranjan", "Cuttack", 32, 10, '23LPA']
chit.insert(0, "Mr.")  # Inserts at the 0th place
print(chit)  # ['Mr.', 'Chittaranjan', 'Cuttack', 32, 10, '23LPA']
chit.append("Maersk")  # Appends at the end
print(chit)  # ['Mr.', 'Chittaranjan', 'Cuttack', 32, 10, '23LPA', 'Maersk']
chit.pop()  # Removes the last element
print(chit)  # ['Mr.', 'Chittaranjan', 'Cuttack', 32, 10, '23LPA']
print(chit.count("Cuttack"))  # 1
chit.remove(10)  # It removes the mentioned element form the list
print(chit)  # ['Mr.', 'Chittaranjan', 'Cuttack', 32, '23LPA']
chit.reverse()  # It reverses all the element
print(chit)  # ['23LPA', 32, 'Cuttack', 'Chittaranjan', 'Mr.']
print(chit.index(32))  # It gives the index of the element
chit.clear()  # It empties the list
print(chit)  # []


print("---------------------------New Section------------------------------")
# a = [2,3,4,5,6,7,6]
# b = [5,6,7,8,9,0]
a = 2
b = 3
print(cmp(a,b))