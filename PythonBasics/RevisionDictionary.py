a = {1: "First Name", 2: "Last Name", "Age": 33}
print(a)
print(a[1])
print(a["Age"])

a["add"] = "Delhi"
print(a)
a["add"] = "Bangalore"
print(a)

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
del student_id[111]
print("Updated Dictionary ", student_id)

print(all(a))  # Return True if all keys of the dictionary are True
print(any(a))  # Return True if any key of the dictionary is true.
print(len(a), len(student_id))  # Return the length (the number of items) in the dictionary.
print(a.keys())  # Returns a new object of the dictionary's keys. - List
print(a.values())  # Returns a new object of the dictionary's values - List

for i in a:
    print(i, " : ", a[i])
