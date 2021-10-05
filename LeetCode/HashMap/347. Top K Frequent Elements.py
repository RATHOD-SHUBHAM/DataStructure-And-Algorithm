"""
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""

import heapq
nums = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,4,4,4,4,4,4,4,5]
k = 2

dict = {}
max_nums = []

# count in dictionary
for i in nums:
    # increase count in dict
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1


print(dict)
'''
heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.

heapq.heappushpop(heap, item)
Push item on the heap, then pop and return the smallest item from the heap. 
The combined action runs more efficiently than heappush() followed by a separate call to heappop().
'''
for key,val in dict.items():
    if len(max_nums) < k:
        heapq.heappush(max_nums, [val,key])
        print(max_nums)
    else:
        heapq.heappushpop(max_nums, [val,key])
        print(max_nums)

print(max_nums)

for value,key in max_nums:
    print(value)
    print(key)
    print("\n")

result = [key for value, key in max_nums]
print(result)


