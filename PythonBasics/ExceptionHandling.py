ItemsInCart = 0
# 2 items will be added to the cart

if ItemsInCart != 2:
    # raise Exception("Product Cart count is not matching.")
    pass
    # raise Exception("Condition is not matching")

assert (ItemsInCart == 0)

try:
    with open('test.txt', 'r') as reader:  # it will throw FileNotFoundError
        reader.read()

except Exception as e:
    print("I am at except block")
    print(e)

finally:
    print("cleaning up resources")
