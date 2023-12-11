from math import sqrt


def greet():
    print("Hello Abhishek ")


def summ(a=5, b=6):
    return a + b


greet()
tot = summ()
print(tot)
print(sqrt(196))
if sqrt(196) == sqrt(pow(14, 2)):
    print('math library is correct')


# Recursive Function
def fact(a):
    if a == 1:
        return 1
    else:
        return a * fact(a - 1)


print(fact(5))