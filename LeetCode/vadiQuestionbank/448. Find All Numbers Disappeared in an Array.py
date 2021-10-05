'''

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space

'''

'''
nums = [4, 3, 2, 7, 8, 2, 3, 1]
n = len(nums)
print(n)
result = []

for i in range(n):
    print(i + 1)
    if i + 1 not in nums:
        result.append(i + 1)
print(result)
'''

nums = [4,3,2,7,8,2,3,1]
missing = []

# list will only have elements that are from 1 to n
# make the elements at that index as negative
# if the element is missing then the value at that particular index will be positive
# keep in mind the index val will be one less than that of the actual value

for i in nums:
    print(" the nums are",i)
    idx = abs(i) - 1            # keep in mind the index val will be one less than that of the actual value
    print("The idx are: ",idx)
    if nums[idx] > 0:
        nums[idx] *= -1
    print(nums)
    print("\n")

for i in range(len(nums)):
    if nums[i] > 0:
        missing.append(i+1)         # keep in mind the index val will be one less than that of the actual value
print(missing)