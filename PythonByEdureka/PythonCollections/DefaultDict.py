from collections import defaultdict

d = defaultdict(int)
d[1] = 'edureka'
d[2] = 'python'

print(d) # o/p - defaultdict(<class 'int'>, {1: 'edureka', 2: 'python'})
print(d[3]) # o/p - 0 - If it was normal dictionary then it would have thrown an error.