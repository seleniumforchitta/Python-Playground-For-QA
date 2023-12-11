# 1. Write a test that creates a folder,
# 2. within the folder create a file,
# 3. write to the file,
# 4. copy the file,
# 5. read from the file,
# 6. count number of words,
# 7. Find unique words and print them
# 8.  get file size
# 9. delete the file
# 10. check if the file exist and print if it exist or not

import os

#os.mkdir("C:\Your_Drive\Test7")
op = open("C:\Your_Drive\Test.txt", 'w')
str = "Test Automation"
op.write(str)
# str1 = ""
op1 = open("C:\Your_Drive\Test.txt", 'r')
str1 = op1.read()



print(str1)
# list1 = str1.split(' ')
# print(len(list1))




