All = [23, 45, 34, 56, 76, 66, 77, 88, 76, 0, 66, 77, 66, 66]
All.sort(reverse=True)
print(All)
print(sorted(All))
All1 = All.copy()
print(All1)
All.remove(0)
print(All)
print(All.count(100))
All.extend(set(All1))
print(All)
All.pop()
print(All)
All.reverse()
print(All)
print(All.index(77))
All.insert(0, 99)
print(All)
All.clear()
print(All)

