print("Hello World")

#prime numbers less than 30

for i in range(2,30):
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count=count+1
    if count==0:
        print(i, "is a prime number")