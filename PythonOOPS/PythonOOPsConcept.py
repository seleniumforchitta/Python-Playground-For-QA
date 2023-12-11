class Computer:

    def __init__(self, cpu, ram):
        # it's like a constructor to initialize variable
        print("in init")
        self.cpu = cpu # You have to convert it to self type variable
        self.ram = ram


    def config(self):
        print("config is - ", self.cpu, self.ram) #you have to use self.variable only


comp1 = Computer('i5',16) # This is like a parameterazied constructor
comp1.config()
comp2 = Computer('Ryzen 5', 8)
comp2.config()
Computer.config(comp1) # This is another way to call a method after creating object

