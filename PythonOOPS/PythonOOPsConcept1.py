class Computer:

    def __init__(self):
        self.name = "Navin"
        self.age = 28

    def update(self, age):
        self.age = age

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
print(id(c1))  # 2166642072816
print(id(c2))  # 2166642073344
c1.name = "Rashi"  # We can change the value of particular object also
c1.age = 23

print(c1.name, c1.age)  # Rashi 23
c1.update(24)
print(c1.name, c1.age)  # Rashi 24
print(c2.name, c2.age)  # Navin 28
c2.update(29)
print(c2.name, c2.age)  # Navin 29

if c1.compare(c2):
    print("They are same")
else:
    print("They are not same")
