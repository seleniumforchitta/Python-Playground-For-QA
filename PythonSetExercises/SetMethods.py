id = {12, 23, 34, 45, 56, 66, 56}
print(id)
id.add(24)
print(id)
empty_set = set()
empty_dictionary = {}
print(type(empty_dictionary))
print(type(empty_set))
print(sorted(id))
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple', 'Lacoste']
companies.update(tech_companies)
print(companies)
id.discard(23)
print(id)
print(sum(id))

# for m in range(10, -1, -1):
#     print(m)

it = 10
while it>0:
    it = it - 1
    if it == 3:
        continue
    print(it)

