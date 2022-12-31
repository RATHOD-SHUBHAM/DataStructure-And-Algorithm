# Tc : O(n) Sc: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        left = 0
        right = n - 1 
        
        while left < right:
            summ = numbers[left] + numbers[right]
            
            if summ == target:
                return [left + 1, right + 1]
            elif summ > target:
                right -= 1
            else:
                left += 1
