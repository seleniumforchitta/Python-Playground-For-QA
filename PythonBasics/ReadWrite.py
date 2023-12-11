# file = open('../test.txt')
# print(file.read())
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# line = file.readlines()
# for i in line:
#     print(i)
# file.close()

with open('../test.txt', 'r') as reader:
    # Goal is to read the file & store in a list. Then reverse the list....
    content = reader.readlines()  # It will store in a list
    reversed(content)  # Reverse the list

with open('../test.txt', 'w') as writer:
    for line in reversed(content):
        writer.write(line)



