# list = test_list = [1, 6, 3, 5, 3, 4]
# Input: 3  # Check if 3 exist or not.
# Output: True
from collections import Counter

numbers = [1, 6, 3, 5, 3, 4]
num = 6
# Using Try Except
try:
    if numbers.index(num):
        print(True)
except:
    print(False)

# Using if in
if num in numbers:
    print(True)
else:
    print(False)

# Using for in
for i in numbers:
    if i == num:
        print(True)

# Using count()
rep = numbers.count(num)
if rep == 0:
    print(False)
else:
    print(True)

# Using find()
new = str(numbers)
if new.find(str(num)) == -1:
    print(False)
else:
    print(True)

# Calculating frequencies - using Counter()
frequency = Counter(numbers)
if frequency[num] > 0:
    print(True)
else:
    print(False)

