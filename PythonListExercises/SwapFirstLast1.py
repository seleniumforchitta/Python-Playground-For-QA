# Given a list, write a Python program to swap first and last element of the list.
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

list1 = [1, 2, 3]
len1 = len(list1) - 1
ele1 = list1[0]
ele2 = list1[len1]
print(ele1, ele2)
list2 = list1.copy()
list2.pop()
list2.append(ele1)
list2.remove(ele1)
list2.insert(0, ele2)

print(list1)
print(list2)
