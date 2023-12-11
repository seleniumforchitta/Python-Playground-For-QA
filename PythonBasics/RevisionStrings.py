greet = 'Hello'

# access character from 1st index to 3rd index
print(greet[1:4])  # "ell"
message = 'Hola Amigos'
# message[0] = 'H' # In Python, strings are immutable.
# That means the characters of a string cannot be changed. For example,
print(message)

# However, we can assign the variable name to a new string. For example,
# assign new string to message variable
message1 = 'Hello Friends'
print(message1)  # prints "Hello Friends"

# multiline string
message = """
Never gonna give you up
Never gonna let you down
"""
print(message)

str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)

greet = 'Hello'
# iterating through greet string
for letter in greet:
    print(letter)

print(len(greet))
print('a' in 'program')  # True - Membership
print(greet.upper())
print(greet.lower())
print(message1.partition(' '))
print(message1.replace('Hello', 'Bye'))
# replacing only two occurrences of 'let'
song = "Let don't let Let Let Let chit"
print(song.replace('Let', "don't let", 2))

# find()	returns the index of first occurrence of substring
print(message.find('fun'))
print(song.find('Let'))
print(song.find('let'))

text = 'Python is a fun programming language'
# split the text from space
print(text.split(' '))
# Output: ['Python', 'is', 'a', 'fun', 'programming', 'language']

pin = "523"
# checks if every character of pin is numeric
print(pin.isnumeric())  # True coz, all the members are numbers

