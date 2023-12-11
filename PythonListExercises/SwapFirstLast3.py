# Given a list, write a Python program to swap first and last element of the list.
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

list1 = [12, 35, 9, 56, 24]
print(list1)
list1[0], list1[-1] = list1[-1], list1[0]
print(list1)

