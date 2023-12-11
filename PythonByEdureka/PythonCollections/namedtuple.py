from collections import namedtuple

a = namedtuple('courses', 'name, skill')
s = a('data science','Python')
print(s)
#using a list to create a namedtuple
p = a._make(['AI','Python'])
print(p)