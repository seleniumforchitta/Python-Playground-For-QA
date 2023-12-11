arr = [2, 3, 3, 4, 5, 6, 7, 8, 9, 8]
num = {2, 3, 3, 4, 5, 6, 7, 8, 9, 8}
# str = "Automation"
# tot = 0
# for i in num:
#     tot = tot + i
#
# print(tot)
# print(sum(num))
# arr.sort(reverse=True)
# print(arr)
# str.find('a')
# print(str.find('a'))
#
# l = dict(zip(arr, list(str)))
# print(l)

iter_obj = iter(arr)
for i in arr:
    print(i, end=", ")
print()
for i in arr:
    print(next(iter_obj), end=", ")

