import random
import math

list = [3,4,5,6,5,3,4,7,8,9,0]
print("Printing random element from a list using choice() method - ",random.choice(list))
print("Printing random number between 0 & 1 using random() method - ",int((random.random()*100)))
print("Printing random number between 0 & 1 using random() method - ",math.floor((random.random()*100)))
print("Printing random number between 0 & 1 using random() method - ",math.ceil((random.random()*100)))
print("Printing random number between 0 & 1 using random() method - ",round((random.random()*100)))


print(math.floor(1.9))
print(math.ceil(1.4))
print(int(1.9))
print(round(1.499))

random.seed(3)
# print a random number between 1 and 1000.
print(random.randint(1, 1000))
# if you want to get the same random number again then,
print(random.randint(1, 1000))
print(random.randint(1, 1000))
print(random.randint(1, 1000))
random.seed(3)
print(random.randint(1, 1000))

print("uniform(int x, int y) - ", random.uniform(4,7))