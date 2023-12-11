from collections import Counter

a = [1,1,2,3,2,3,2,4,5,6,4,5,6,7,7,7,8]
c = Counter(a)
print(c) # o/p - Counter({2: 3, 7: 3, 1: 2, 3: 2, 4: 2, 5: 2, 6: 2, 8: 1})
print(list(c.elements())) # Returns all the elements present in the counter
# o/p - [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8]
print(c.most_common()) # To get asserted list. o/p - [(2, 3), (7, 3), (1, 2), (3, 2), (4, 2), (5, 2), (6, 2), (8, 1)]
sub = {2:1,6:1}
c.subtract(sub) # it will subtract 2, 1 time & 6 1 time
print(c.most_common()) # o/p - [(7, 3), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 1), (8, 1)]
