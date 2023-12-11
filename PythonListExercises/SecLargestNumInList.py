abc = [23, 34, 54, 56, 67, 76, 75]

large = abc[0]
sec = abc[0]
for i in abc:
    if i > large:
        large = i
for i in abc:
    if sec < i < large:
        sec = i

print("largest =", large, "\nSecond Largest =", sec)
