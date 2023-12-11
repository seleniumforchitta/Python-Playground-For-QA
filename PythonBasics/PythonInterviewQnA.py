import sys

import idna.idnadata

a = 10
b = a
c = b

print(sys.version)  # 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)]
print(sys.getrefcount(a)) # 18

a = [100,200,300,400,500,600,700]
print(a[0::2])
num = ','.join(str(i) for i in a)
print(num)