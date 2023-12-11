import copy

li1 = [23, [45, 67], 78, 89]
li2 = copy.copy(li1)
li3 = copy.deepcopy(li1)
print(li2)
print(li3)
print(id(li1[1]))
print(id(li2[1]))  # soft copy so address of each element is still same
print(id(li3[1]))  # deep copy so address of each element is different

li1[1][0] = 20
print(li1)  # [23, [20, 67], 78, 89]
print(li2)  # [23, [20, 67], 78, 89] # in shallow copy the address of inner element is same, so value is not changed.
print(li3)  # [23, [45, 67], 78, 89] # in deep copy the address is different, so value is unchanged.

li1[0] = 21
print(li1)  # [21, [20, 67], 78, 89]
print(li2)  # [23, [20, 67], 78, 89]
print(li3)  # [23, [45, 67], 78, 89]
