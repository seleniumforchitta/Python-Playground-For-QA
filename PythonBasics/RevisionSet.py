# A set is a collection of unique data. That is, elements of a set cannot be duplicate.
# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# create an empty set
empty_set = set()
# create an empty dictionary
empty_dictionary = {}
# check data type of empty_set
print('Data type of empty_set:', type(empty_set))
# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))

numbers = {2, 4, 6, 6, 2, 8}
print(numbers)  # {8, 2, 4, 6}

numbers = {21, 34, 54, 12}
print('Initial Set:', numbers)
# using add() method
numbers.add(35)
print('Updated Set:', numbers)
print(sorted(numbers))  # [12, 21, 34, 35, 54]

# The update() method is used to update the set with items
# other collection types (lists, tuples, sets, etc). For example,

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple', 'Lacoste']
companies.update(tech_companies)
print(companies)
# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}
print(sorted(companies))  # ['Lacoste', 'Ralph Lauren', 'apple', 'google']

# Remove an Element from a Set - discard()
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:', languages)
# remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove():', languages)

# Union, Intersection, Difference & Symmetric
# first set
A = {1, 3, 5}
# second set
B = {0, 2, 4}
# perform union operation using |
print('Union using |:', A | B)  # {0, 1, 2, 3, 4, 5}
# perform union operation using union()
print('Union using union():', A.union(B))  # {0, 1, 2, 3, 4, 5}

# first set
A = {1, 3, 5}
# second set
B = {1, 2, 3}
# perform intersection operation using &
print('Intersection using &:', A & B)  # {1, 3}
# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))  # {1, 3}

# first set
A = {2, 3, 5}
# second set
B = {1, 2, 6}
# perform difference operation using &
print('Difference using &:', A - B)  # {3, 5}
# perform difference operation using difference()
print('Difference using difference():', A.difference(B))  # {3, 5}

# The symmetric difference between two sets A and B includes
# all elements of A and B without the common elements.
# first set
A = {2, 3, 5}
# second set
B = {1, 2, 6}
# perform difference operation using &
print('using ^:', A ^ B)  # {1, 3, 5, 6}
# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))  # {1, 3, 5, 6}

languages = ['Python', 'Java', 'JavaScript']
enumerate_prime = enumerate(languages)
# convert enumerate object to list
print(list(enumerate_prime))
# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

# Python sum()
marks = [65, 71, 68, 74, 61]  # find sum of all marks
total_marks = sum(marks)
print(total_marks)  # Output: 339
# print(sum(languages)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Check if two sets are equal
# first set
A = {1, 3, 5}
# second set
B = {3, 5, 1}
# perform difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')  # o/p = Set A and Set B are equal

# copy
numbers = {1, 2, 3, 4}
# copies the items of numbers to new_numbers
new_numbers = numbers.copy()
print(new_numbers)
# Output:  {1, 2, 3, 4}

# issubset()
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
# all items of A are present in B
print(A.issubset(B))
# Output: True

