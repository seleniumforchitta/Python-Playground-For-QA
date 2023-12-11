# Add two lists, alternating elements. If one of the lists is longer than the other, all items should be added to the end:
# a = [1, 2, 3, 4, 5]
# b = [4, 6, 8]
# Result example: c = [1, 4, 2, 6, 3, 8, 4, 5]
a = [1, 2, 3, 4, 5]
b = [4, 6, 8, 3, 3, 0, 0, 0]
la = len(a)
lb = len(b)
lc = min(la, lb)
c = []

for i in range(0, lc):
    c.append(a[i])
    c.append(b[i])

for j in range(lc, max(la, lb)):
    if la > lb:
        c.append(a[j])
    else:
        c.append(b[j])

print(c)
