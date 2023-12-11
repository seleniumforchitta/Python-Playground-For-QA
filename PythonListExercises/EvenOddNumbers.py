# Python program to print even numbers in a list
# Python program to print odd numbers in a List
# Python program to print all even numbers in a range
# Python program to print all odd numbers in a range
# Python program to count Even and Odd numbers in a List

All = [23, 45, 34, 56, 76, 66, 77, 88, 9, 0, 33]
even = []
odd = []

for i in All:
    if i % 2 == 0 and i != 0:
        even.append(i)
    elif i % 2 != 0 and i != 0:
        odd.append(i)
print(even)
print(odd)

ev = [a for a in All if a % 2 == 0 and a != 0]
print(ev)

even1 = 0
odd1 = 0
for i in range(1, 100):
    if i % 2 == 0:
        # print(i, " is even")
        even1 = even1 + 1
    else:
        # print(i, " is odd")
        odd1 = odd1 + 1
print(even1, odd1)
