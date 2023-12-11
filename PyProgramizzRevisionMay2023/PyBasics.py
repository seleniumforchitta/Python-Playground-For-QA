""" I
am a multi line comment """

# I am a single line comment

# Python is a type-inferred language, so you don't have to explicitly define the variable type

a, b, c = 2, 5, "rama"

mylist = [2, 3, 4, 5, 6]
mytuple = (2, 3, 4, 5, 7)
mydict = {1: 3, 2: 34, 3: 45, 4: 56}
myset = {2, 3, 4, 4, 5, 6}
mystr = "Abhishek  Mishra "

print(mylist)
print(mytuple)
print(mydict.keys())
print(myset)

print('New Year', 2023, 'See you soon!', sep='. ')
print('Good Morning')

summ = 0
for x in mylist:
    print(x, end=" ")
    summ = summ + x
print()
print(summ)

a = 20
while a > 0:
    print(a, end=' ')
    a = a - 1
print()
for p in range(20, 0, -1):
    if p % 2 == 0:
        continue
    print(p, end=' ')
