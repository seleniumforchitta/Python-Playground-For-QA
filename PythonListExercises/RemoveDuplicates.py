# Remove multiple elements from a list in Python
All = [23, 45, 34, 56, 76, 66, 77, 88, 76, 0, 66, 77, 66, 66]
SetList = []
setL = set(All)
print(setL)

for i in All:
    if i not in SetList:
        SetList.append(i)

print(sorted(SetList))
