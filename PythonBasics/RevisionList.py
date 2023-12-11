b, c, d = 5, 4.5, "Great"
print(b, c, d)

a = 5
v = 6
e = 90
print(a, v, e)

c = [1, 2, 3, 4, "kuch", "bhi"]
print(type(c), c)
print(c[-1::-1])
print(c[0:len(c):1])
c.insert(1, "chitta")
print(c)
c.append(33)
c.append(b)
print(c)
del c[-1]
print(c)
c[0] = "1st"
print(c)
c.pop()
print(c)
print(c.count(2))
print(c.count(b))
c.remove(2)
print(c)
c.reverse()
print(c)
print(c.index(4))

