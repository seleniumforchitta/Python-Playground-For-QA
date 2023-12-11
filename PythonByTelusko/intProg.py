arr = [2, 0, 3, 0, 4, 4, 4, 0, 0, 5, 0, 6, 0]

for i in arr:
    if i == 0:
        arr.remove(i)
        arr.append(i)

print(arr)

arr.reverse()
print(sorted(arr))

names = ['john', 'meena', 'jacob', 'teena', 'meenu', 'pj', 'jjj', 'tjjj']
names1 = []
for i in names:
    if i.startswith('j'):
        names1.append(i)

print(names1)

a = "ramaranjan Swain is a good boy"
b = a[0]
for i in a:
    if i not in b:
        b = b+i

print(len(b))
print(len(set(a)))

