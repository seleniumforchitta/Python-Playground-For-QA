try:
    x = input("Enter first Number : ")
    y = input("Enter second Number : ")
    print("values stored are - ",x,y)
    res = int(x)/int(y)
    print("The result of 2 divided number - ", res)
except ZeroDivisionError:
    print("ZeroDivisionError - ",ZeroDivisionError)
except TypeError:
    print("TypeError - ",TypeError)
except NameError:
    print("NameError - ", NameError)
except Exception:
    print("Exception - ", Exception)
else:
    print("Else Block is executed.")
finally:
    print("Finally is executed")
