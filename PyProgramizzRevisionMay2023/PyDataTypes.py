name = 'ramaranjan'
mylist = []
for i in name:
    mylist.append(i)
print(mylist)
print(mylist[int(len(mylist) / 2):len(mylist):1])

List1 = [2, 3, 5, 5, 5, 5, 5]
List2 = [4, 6, 8, 7, 9]
List3 = []
if len(List1) < len(List2):
    llen = len(List1)
else:
    llen = len(List2)

for i in range(0, llen):
    List3.append(List1[i])
    List3.append(List2[i])

if len(List1) < len(List2):
    List3.extend(List2[llen:len(List2)])
else:
    List3.extend(List1[llen:len(List1)])

print(List3)

numbers = [number for number in range(1, 100) if number % 5 == 0]
print(numbers)

nums = [num**2 for num in range(1, 10)]
print(nums)


