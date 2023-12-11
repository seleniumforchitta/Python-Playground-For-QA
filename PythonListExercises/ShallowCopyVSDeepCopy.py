import copy

a = [[2,3,4,5],[6,7,8,9]]
b = a.copy()
c = copy.deepcopy(a)

a[0][0] = 1

print(a)
print(b)
print(c)