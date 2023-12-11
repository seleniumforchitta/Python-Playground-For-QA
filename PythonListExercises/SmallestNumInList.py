l1 = [123, 234, 45, 567, 6789, 8]

small = l1[0]
for ele in l1:
    if ele < small:
        small = ele

print(small)
print(min(l1))

l1.sort()
print(l1[0])

l1.sort(reverse=True)
print(l1[-1])

