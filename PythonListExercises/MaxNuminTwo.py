# Python program to find the
# maximum of two numbers

# Driver code
a = 2
b = 4

# Use of ternary operator
print(a if a >= b else b)

# Use of max()
print(max(a, b))

# Use of lambda
greater = lambda c, d: c if c >= d else d
print(greater(a, b))

# Use of sort()
x = [a, b]
x.sort()
print(x[-1])


