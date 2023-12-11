from OopsDemo import Calculator


class ChildClass(Calculator):
    num2 = 200

    def __init__(self):
        print("I am in Child class const - ")
        Calculator.__init__(self, 20, 30)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


obj = ChildClass()
print("The Total sum is = ", obj.getCompleteData())
