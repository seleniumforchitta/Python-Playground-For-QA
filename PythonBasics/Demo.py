# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.
# 	Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: nums = [0,1,3,0,4,_,_,_]


nums = [0, 1, 2, 2, 3, 0, 4, 2]
nums1 = []
nums2 = []
val = 2
for i in nums:
    if i != val:
        nums1.append(i)
    else:
        nums2.append('_')
nums1.extend(nums2)
print(nums1)



