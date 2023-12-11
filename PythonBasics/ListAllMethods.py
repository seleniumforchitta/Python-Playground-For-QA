nums = [3,5,6,8,4,3,6,9]
nums.append(7) # Appends to the end and takes 1 arg
print(nums)
print(nums.count(3)) # Counts how many times given value is present in the list
num1 = [2,3,4]
nums.extend(num1) # Adds another list to the end
print(nums)
print(nums.index(3)) # Returns first occuramnce of given value in the list
nums.insert(1,7) # Inserts at a specific index. 1st arg = index, 2nd arg = val
print(nums)
print(nums.pop()) # Pops & returns last value of the list
print(nums)
nums.remove(7) # removes first occurance of the value
print(nums)
nums.reverse() # Reverses the complete list
print(nums)
nums.sort()
print(nums)
print(sorted(nums, reverse = True))