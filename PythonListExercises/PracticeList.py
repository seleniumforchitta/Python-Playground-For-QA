from collections import Counter

l1 = [3, 4, 5, 6, 7, 3]
num = 6
# check if 6 is there in the list
try:
    if l1.index(num):
        print(True)
except:
    print(False)

if num in l1:
    print(True)
else:
    print(False)

if l1.count(num) > 0:
    print(True)
else:
    print(False)

for i in l1:
    if i == num:
        print(True)

if str(l1).find(str(num)) == -1:
    print(False)
else:
    print(True)

frequency = Counter(l1)
if frequency[num] > 0:
    print(True)
else: print(False)

ev = [i for i in l1 if i%2 ==0 and i!=0]
print(ev)

l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

l2.reverse()
print(l2)
print(l2[-1::-1])

abc = [23, 34, 54, 56, 67, 76, 75]
lar = abc[0]
for i in abc:
    if i > lar:
        lar = i
print(lar, max(abc))
