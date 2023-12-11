try:
    numerator = int(input("Please enter the Numerator : "))
    Denominator = int(input("Please enter the Denominator : "))

    result = numerator / Denominator
    print(result)

    li = [1, 2, 3]
    i = int(input("Enter the index you want to access : "))
    print(li[i])
except ZeroDivisionError:
    print("Denominator can't be zero")

except IndexError:
    print("Index can't be greater than the size of the array")

finally:
    print("I am finally Bro")
print("Program ends")
