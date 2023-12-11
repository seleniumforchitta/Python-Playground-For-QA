fd = open('C:\\Users\\chitt\\PycharmProjects\\pythonTesting\\PythonBasics\\Maersk.txt','w')
print(fd.name)
print(fd.mode)
text= "It is a shipping & logistics company."
fd.writelines(text)
fd.close()