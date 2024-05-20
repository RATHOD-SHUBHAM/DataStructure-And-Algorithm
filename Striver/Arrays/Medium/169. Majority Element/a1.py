# Sorting 
# Tc: O(nlogn) | Sc: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return nums

        nums.sort()

        left = 0
        right = n - 1

        mid = left + (right - left) // 2

        return nums[mid]
    
# ------------------------------------------------------------

# Mode calculation

# Tc and Sc: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        n = len(nums)

        for i in range(n):
            cur_num = nums[i]

            if cur_num in dic:
                dic[cur_num] += 1
            else:
                dic[cur_num] = 1
        
        return max(dic)
    
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        dic = collections.defaultdict(int)

        for i in range(n):
            dic[nums[i]] += 1
        
        return max(dic)

'''

# ------------------------------------------------------------

# Using counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        dic = collections.Counter(nums)
        
        # print(max(dic, key = lambda x: dic.get(x)))

        return max(dic, key = lambda x : dic.get(x))       

# ------------------------------------------------------------

# Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        majority_ele = None

        for i in range(n):
            if count == 0:
                majority_ele = nums[i]
                count += 1
            
            elif nums[i] == majority_ele:
                count += 1
            else:
                count -= 1
        
        # You may assume that the majority element always exists in the array.
        return majority_ele

        '''
        # if there is no gurantee that majority element always exists then
        
        # check if this is the majority element
        count_of_majority_ele = 0
        for i in range(n):
            if majority_ele == nums[i]:
                count_of_majority_ele += 1
        
        if count_of_majority_ele > (n/2):
            return majority_ele
        else:
            return -1
        '''