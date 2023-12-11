name = "rama Kumar  Mishra "
words = name.split(' ')
newName = ""
for i in range(len(words) - 1, -1, -1):
    newName = newName + str(words[i]) + " "
print(newName)
print(name.find('Kumar '))
print(words)
print(str(words))
print(str(words).find('Kumar '))
pin = '753008'
print(pin.isnumeric())