# Python program to demonstrate
# calling the parent's class method
# inside the overridden method


class Parent:

    def __init__(self):
        print("Inside Parent const")


class Child(Parent):

    def __init__(self):
        # Calling the parent's class
        # method
        print("Inside Child const")
        Parent.__init__(self)


# Driver's code
obj = Child()
