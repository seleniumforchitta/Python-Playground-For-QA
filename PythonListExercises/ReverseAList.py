# reversed a list
# Input: list = [4, 5, 6, 7, 8, 9]
# Output : [9, 8, 7, 6, 5, 4]

# using reverse()
nums = [4, 5, 6, 7, 8, 9]
nums.reverse()
print(nums)

# using index
nums = [4, 5, 6, 7, 8, 9]
print(nums[-1::-1])

# using for loop, index and pop()
nums = [4, 5, 6, 7, 8, 9]
newNums = []
for i in range(0, len(nums)):
    newNums.append(nums.pop())
print(newNums)

# using while & pop()
nums = [4, 5, 6, 7, 8, 9]
newNums = []
while len(nums) > 0:
    newNums.append(nums.pop())
print(newNums)

# inserting at 0th position
nums = [4, 5, 6, 7, 8, 9]
newNums = []
for i in nums:
    newNums.insert(0, i)
print(newNums)