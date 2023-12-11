from collections import ChainMap

a = {1:'edureka',2:'Python'}
b = {3:'ML',4:'AI'}

a1 = ChainMap(a ,b) # single view of multiple mappings
print(a1)  # o/p - ChainMap({1: 'edureka', 2: 'Python'}, {3: 'ML', 4: 'AI'})