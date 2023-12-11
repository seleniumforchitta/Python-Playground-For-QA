# List is same like arrays

values = [1, 2, 3, "rahul", 777, 8.89]
"""
print(values[0])
print(values[1])
print(values[2])
print(values[3])
print(values[4])
print(values[5])
print(values[-1])
print(values[1:4])
"""
values.insert(4, "chitta")

print(values)

values.append("last")
print(values[0::1])  # it will traverse from 0 to the end of list with a gap of 1
print(values[-1::-1])  # it will start from end  of  list to the start with a gap of 1

del values[0]
print(values)

val = (4, 5, 6, "me")
print(val[0])

a = {1: "first name", 2: "last name", "age": 33}
# print value having key=1
print(a[1])
# print value having key=2
print(a[2])
# print value having key="age"
print(a["age"])
