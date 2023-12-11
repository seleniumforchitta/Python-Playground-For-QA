import sys

str = "@#dd$$frt%%GTy^*chit#a"
str1 = ""
for i in str:
    if i.isalnum():
        str1 = str1 + i
print(str1)
str2 = input("Enter a string")
print(str2)
str3 = sys.stdin.readline()
print(str3)
