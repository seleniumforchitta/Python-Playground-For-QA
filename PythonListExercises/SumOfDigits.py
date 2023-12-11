l1 = [123,234,45,567,6789]
l2 = []

for ele in l1:
    tot = 0
    for j in str(ele):
        tot = tot+int(j)
    l2.append(tot)

print(l1)
print(l2)

# find sum & avg of a list
tot = 0
for ele in l1:
    tot = tot+ele
avg = tot/len(l1)
print(tot)
print(avg)




