name = "rama Ranjan Swain"
words = name.split(' ')
newName = ""
for i in range(len(words) - 1, -1, -1):
    newName = newName + str(words[i]) + " "
print(newName)
print(name.find('Ranjan'))
print(words)
print(str(words))
print(str(words).find('Ranjan'))
pin = '753008'
print(pin.isnumeric())