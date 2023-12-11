# Python program to print positive numbers in a list
# Python program to print negative numbers in a list
# Python program to print all positive numbers in a range
# Python program to print all negative numbers in a range
# Python program to count positive and negative numbers in a list
All = [23, -45, 34, -56, 76, -66, -77, -88, 9, 0, 33]
pos = []
posc = 0
neg = []
negc = 0
for i in All:
    if i < 0:
        neg.append(i)
        negc += 1
    else:
        pos.append(i)
        posc += 1

print(pos, posc)
print(neg, negc)
