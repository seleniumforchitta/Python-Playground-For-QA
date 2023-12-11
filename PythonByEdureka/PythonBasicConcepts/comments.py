'''
File-name: mymodule.py
Functions: greet(name)
'''
def greet(name=None):
    '''This method greets a person.
    Parameters:
        name (string): name of the person
    '''
    #before greeting check if name is not null
    if name is not None:
        print('Hello!', name)
    else:
        print('Welcome!')

greet(input("Enter your name - "))