def div(a, b):
    return a / b


def smartdiv(func, a, b):
    if a < b:
        a, b = b, a
    return func(a, b)


div = smartdiv(div, 2, 4)
