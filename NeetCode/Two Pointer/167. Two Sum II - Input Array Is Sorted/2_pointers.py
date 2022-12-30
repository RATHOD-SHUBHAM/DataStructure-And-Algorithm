# Tc: O(n) and Sc:O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 1:
            return numbers
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            summ = numbers[left] + numbers[right]
            
            if summ == target:
                return [left + 1, right + 1] # 1 indexed
            elif summ > target:
                right -= 1
            else:
                left += 1
                
        return [-1, -1]