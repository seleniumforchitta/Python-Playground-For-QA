# Python program to find the
# maximum of two numbers

# Driver code
a = 2
b = 4

# Ternary operator
print(a if a <= b else b)

# Min()
print(min(a, b))

# Lambda
smaller = lambda c, d: c if c <= d else d
print(smaller(a, b))

# sort()
x = [a,b]
x.sort()
print(x[0])