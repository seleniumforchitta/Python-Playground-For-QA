import json
book = {}
book['rama'] = {
    'name': 'rama',
    'address': 'Bangalore, Karnataka',
    'phone': 9898989898
}
book['Ambuja'] = {
    'name': 'Ambuja',
    'address': 'Mysore, Karnataka',
    'phone': 7979797979
}
s = json.dumps(book)
print(s)
print(type(s))

with open("C:/Users/ram/OneDrive/Desktop/a.txt", "w") as f:
    f.write(s)

