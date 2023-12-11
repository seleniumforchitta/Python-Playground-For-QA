# Given a list in Python and provided the positions of the elements,
# write a program to swap the two elements in the list.
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]
#
# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]

list1 = [23, 65, 19, 90]
pos1 = 1
pos2 = 3
list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
print(list1)

list2 = [1, 2, 3, 4, 5]
pos1 = 1
pos2 = 4
temp = list2[pos1]
list2[pos1] = list2[pos2]
list2[pos2] = temp
print(list2)
