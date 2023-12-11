num = int(input("Enter a number to check if it is prime number: "))
count = 0
for i in range(2, num):
    if num%i == 0:
        print("It is not a prime number")
        count = count+1
        break
if count==0:
    print("It is prime number")
