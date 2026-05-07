# Method 1
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        ans.extend(nums)
        ans.extend(nums)

        return ans
    
 # Method 2
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums
    
# Method 3
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
    
# Method 4
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
