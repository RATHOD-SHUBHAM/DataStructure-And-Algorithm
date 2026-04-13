# Tc: O(n) | Sc: O(1)

# Using For Loop
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        
        sum_of_ele = 0

        for i in range(left, right + 1):
            sum_of_ele += self.nums[i]
        
        return sum_of_ele


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# ---------------------------------- ------------------ ------------------- ------------------ -
# Tc: O(1) | Sc: O(1)
# The pre-computation done in the constructor takes O(n) time. Each sumRange query's time complexity is O(1) as the look up operation is constant time.

# Using PreFix Sum
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        for i in range(1, len(self.nums)):
            self.nums[i] = self.nums[i-1] + self.nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        
        sum_of_ele = self.nums[right] - (self.nums[left - 1] if left != 0 else 0)

        return sum_of_ele

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)