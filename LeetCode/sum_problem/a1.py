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