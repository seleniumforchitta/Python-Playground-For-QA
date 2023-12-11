# using equals
import copy

li1 = [4, 8, 2, 10, 15, 18]
li2 = li1
print(li2)

# using copy()
li1 = [4, 8, 2, 10, 15, 18]
li2 = li1.copy()
print(li2)

# using [:]
li1 = [4, 8, 2, 10, 15, 18]
li2 = li1[:]
print(li2)

# using extend()
li1 = [4, 8, 2, 10, 15, 18]
li2 = []
li2.extend(li1)
print(li2)

# using shallow copy
li1 = [4, 8, 2, 10, 15, 18]
li2 = copy.copy(li1)
print(li2)

# using deep copy # This is the slowest method of copying
li1 = [4, 8, 2, 10, 15, 18]
li2 = copy.deepcopy(li1)
print(li2)

# using in
li1 = [4, 8, 2, 10, 15, 18]
li2 = [i for i in li1]
print(li2)

# using append
li1 = [4, 8, 2, 10, 15, 18]
li2 = []
for i in li1: li2.append(i)
print(li2)

# Using map function
li1 = [4, 8, 2, 10, 15, 18]
li2 = map(int, li1)
print(*li2)

# using slice
li1 = [4, 8, 2, 10, 15, 18]
li2 = li1[slice(len(li1))]
print(li2)
