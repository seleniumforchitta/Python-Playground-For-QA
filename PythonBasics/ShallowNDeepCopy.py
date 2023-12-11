import copy
a = [20,30,40]
b = [60,70,80]
c = [a ,b]
e = copy.deepcopy(c) # Check with Shallow copy, deep copy & reference copy
print(id(c))
print(id(c[0]))
print(id(c[1]))
print(id(e))
print(id(e[0]))
print(id(e[1]))
c.append([50,50])
print(c)
print(e)

