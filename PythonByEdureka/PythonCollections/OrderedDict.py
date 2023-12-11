from collections import OrderedDict
d = OrderedDict()
d[1] = 'e'
d[2] = 'd'
d[3] = 'u'
d[4] = 'r'
d[5] = 'e'
d[6] = 'k'
d[7] = 'a'

print(d) # o/p - OrderedDict([(1, 'e'), (2, 'd'), (3, 'u'), (4, 'r'), (5, 'e'), (6, 'k'), (7, 'a')])
print(d.keys()) # o/p - odict_keys([1, 2, 3, 4, 5, 6, 7])
print(d.values()) # o/p - odict_values(['e', 'd', 'u', 'r', 'e', 'k', 'a'])
d[1] = 'p'
print(d) # o/p - OrderedDict([(1, 'p'), (2, 'd'), (3, 'u'), (4, 'r'), (5, 'e'), (6, 'k'), (7, 'a')])