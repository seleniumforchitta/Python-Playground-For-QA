def add2Num(a = 10, b = 20):
    return a + b


print(add2Num(4))


def findAvg(list):
    fAvg = 0
    for i in list:
        fAvg = fAvg + i
    return fAvg / len(list)


print(findAvg([4, 4, 4]))

def fact(a):
    if a==1:
        return 1
    else:
        return a*fact(a-1)

print(fact(5))
