class Calculator:
    num = 100

    # default Constructor
    def __init__(self):
        print("I am now executing inside a constructor.")

    def __init__(self, a, b):
        self.fistNum = a
        self.secNum = b
        # Here fistNum & secNum are instance Variable.
        print("Parameterized Constructor.")

    def getData(self):
        print("I am now executing as a method in class.")

    def summation(self):
        return self.fistNum + self.secNum + Calculator.num


obj1 = Calculator(10, 20)
obj = Calculator(30, 40)
obj.getData()
print(obj.summation())
print(obj1.summation())
