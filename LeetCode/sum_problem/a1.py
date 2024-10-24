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