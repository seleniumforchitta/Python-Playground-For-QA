class Car:
    # if you declare a variable outside init and inside a class, it is called class variable
    wheels = 4

    def __init__(self):
        # if you define a variable inside init() it is called instance variable
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 11

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
