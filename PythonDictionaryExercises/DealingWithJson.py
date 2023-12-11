import json
book = {}
book['Chitta'] = {
    'name': 'Chitta',
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

with open("C:/Users/chitt/OneDrive/Desktop/a.txt", "w") as f:
    f.write(s)

