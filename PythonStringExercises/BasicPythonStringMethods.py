a = " ramaranjan Swain  "

for i in a:
    print(i)

print('C' in a)
print(a.lower())
print(a.upper())
print(a.find('ran'))
print(a.replace('ran', 'kan'))
print(a.startswith('Ch'))
print(a.isnumeric())
print(a.index('n'))
print(a.lstrip())
print(a.partition('ran'))  # Returns a tuple
print(a.split(' '))


str =" geeks quiz practice code"
li = str.split(' ')
str1 = ""
li = li[-1::-1]
for i in range(0, len(li)):
    str1 = str1 + " " +li[i]
print(str1)
print(str)