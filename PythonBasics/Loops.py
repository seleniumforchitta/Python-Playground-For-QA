# For loops

obj = [3, 45, 56, 54, 23]

for i in obj:
    print(i)
i = 0
for j in obj:
    i = i + j
print(i)

i = 0
for j in range(1, 10):
    i = i + j
print(i)

i = 0
for j in range(0, 10, 2):
    # i = i + j
    print(j)


for m in range(10):
    print(m)

# While loop
it = 5
while it > 0:
    it = it - 1
    print(it)

print("While loop started.")
it = 4
while it>1:
    if it != 3:
        print(it)
    it = it - 1
print("While loop completed.")

print("Break program started.")
it = 10
while it > 1:
    if it == 3:
        break
    print(it)
    it = it - 1
print("Break program completed.")

print("Continue program started.")
it = 10
while it > 1:
    it = it - 1
    if it == 5:
        continue
    print(it)
print("Continue program completed.")

