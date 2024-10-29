# ------------------------------ Two Sum ------------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        dic = {}

        for i in range(n):
            diff = target - nums[i]

            if diff in dic:
                return [i, dic[diff]]
            
            dic[nums[i]] = i


# ------------------------------ Two Sum II ------------------------------
# Input Array Is Sorted
#  
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        left = 0
        right = n - 1

        while left < right:
            cur_sum = numbers[left] + numbers[right]

            if cur_sum == target:
                return [left + 1, right + 1]
            elif cur_sum > target:
                '''Reduce the current sum'''
                right -= 1
            else:
                '''Increase the current sum'''
                left += 1


class Solution:
    def __init__(self):
        self.op = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()

        for i in range(n - 2):
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(i, nums, n)
            
        
        return self.op
    
    def twoSum(self, i, nums, n):
        left = i + 1
        right = n - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]

            if cur_sum == 0:
                self.op.append([nums[i] , nums[left] , nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                
            elif cur_sum > 0:
                right -= 1
            
            else:
                left += 1
# ------------------------------ Two Sum III ------------------------------

class TwoSum:

    def __init__(self):
        self.dic = {}
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)
        

    def find(self, value: int) -> bool:
        print(self.dic)
        for i in range(len(self.nums)):
            diff = value - self.nums[i]
            
            if diff in self.dic:
                self.dic.clear()
                return True
            
            self.dic[self.nums[i]] = i
            
        self.dic.clear()
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

# ------------------------------ Two Sum IV ------------------------------
# yet to solve


# ------------------------------ Two Sum Less than K ------------------------------
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n < 2:
            return -1

        nums.sort()

        left = 0
        right = n - 1

        max_sum = -1

        while left < right:
            cur_sum = nums[left] + nums[right]

            if cur_sum >= k:
                '''Reduce the sum'''
                right -= 1
            elif cur_sum < k:
                '''Capture and Increase the sum'''
                left += 1
                max_sum = max(max_sum, cur_sum)
        
        return max_sum

# ------------------------------ Three Sum  ------------------------------

class Solution:
    def __init__(self):
        self.op = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()

        for i in range(n - 2):
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(i, nums, n)
            
        
        return self.op
    
    def twoSum(self, i, nums, n):
        left = i + 1
        right = n - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]

            if cur_sum == 0:
                self.op.append([nums[i] , nums[left] , nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                
            elif cur_sum > 0:
                right -= 1
            
            else:
                left += 1


# ------------------------------ Three Sum Smaller ------------------------------

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        count = 0

        for i in range(n):

            left = i + 1 
            right = n - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if cur_sum < target:
                    count += 1
                    # we know all the elements in between will also result in sum less than target.
                    count += (right - left - 1) 
                    left += 1
                else:
                    right -= 1

        return count 
    
# ------------------------------ Three Sum Closest ------------------------------

# Tc: O(n ^ 2) | Sc: O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        difference = math.inf
        op = 0

        for i in range(n):

            left = i + 1 
            right = n - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                
                # Find out if the cur sum is closest to target
                cur_diff = abs(target - cur_sum)
                if cur_diff < difference:
                    difference = cur_diff
                    op = cur_sum
                
                # Goal is to move closer to the target
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1

        return op 
    
# ------------------------------ Four Sum ------------------------------

class Solution:
    def __init__(self):
        self.op = []

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        n = len(nums)

        for i in range(n-3):
            if i == 0 or nums[i] != nums[i-1]:
                self.threeSum(i, n, nums, target)
        
        return self.op
    
    def threeSum(self, i, n, nums, target):

        for j in range(i+1, n-2):
            if j == i + 1 or nums[j] != nums[j-1]:
                self.twoSum(i, j, n, nums, target)
    
    def twoSum(self, i, j, n, nums, target):
        left = j + 1
        right = n - 1

        while left < right:
            cur_sum = nums[i] + nums[j] + nums[left] + nums[right]

            if cur_sum > target:
                right -= 1
            
            elif cur_sum < target:
                left += 1
            
            else:
                self.op.append([nums[i] , nums[j] , nums[left] , nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1


# ------------------------------ Four Sum II------------------------------

"""
After you solve 4Sum, an interviewer can follow-up with 5Sum II, 6Sum II, and so on. 
What they are really expecting is a generalized solution for k input arrays.
"""

from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        group_list = [nums1, nums2, nums3, nums4] # this group can be of k len
        
        k = len(group_list) // 2
        
        left_half_group = group_list[ : k]
        right_half_group = group_list[k : ]
        print(left_half_group)
        # print(right_half_group)
        
        # Count of a+b
        a = self.k_sum_count(left_half_group)
        print("a: ", a)
        # Count of c+d
        b = self.k_sum_count(right_half_group)
        print("b",b)
        
        # count the number of combination (a+b)-(c+d) = 0
        no_of_combinations = 0
        for _sum in a:
            left_sum = a[_sum]
            right_sum = b[-_sum] if -_sum in b else 0
            
            no_of_combinations += left_sum * right_sum
            
        return no_of_combinations
    
    def k_sum_count(self, half_group):
        prev_sum_count = {0 : 1} # keep track of sum & their number of occurance(Count)
        
        for lst in half_group:
            cur_sum_count = {}
            
            for num in lst:
                for prev_sum in prev_sum_count:
                    cur_sum = num + prev_sum # new_key= a + b
                    
                    if cur_sum not in cur_sum_count:
                        cur_sum_count[cur_sum] = 0
                    
                    cur_sum_count[cur_sum] += prev_sum_count[prev_sum] # new value = count of a + count of b
                    
            prev_sum_count = cur_sum_count
            # print(prev_sum_count)
            
        return prev_sum_count
            
            
        
            