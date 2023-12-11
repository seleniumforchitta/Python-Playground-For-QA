from collections import deque

a = ['e','d','u','r','e','k','a']
d = deque(a)
print(d)  # o/p - deque(['e', 'd', 'u', 'r', 'e', 'k', 'a'])
d.append('Python')
print(d)  # o/p - deque(['e', 'd', 'u', 'r', 'e', 'k', 'a', 'Python'])
d.appendleft('Python')
print(d)  # o/p - deque(['Python', 'e', 'd', 'u', 'r', 'e', 'k', 'a', 'Python'])
d.pop()
print(d)  # o/p - deque(['Python', 'e', 'd', 'u', 'r', 'e', 'k', 'a'])
d.popleft()
print(d)  # o/p - deque(['e', 'd', 'u', 'r', 'e', 'k', 'a'])