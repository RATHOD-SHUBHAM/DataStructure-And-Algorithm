'''
    Existing solutions do not make use of the property that the input array is sorted. We can do better.

    Cant use dictionary as it says:
        Your solution must use only constant extra space.
'''

# Tc: O(n) | Sc: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        left = 0 
        right = n - 1


        while left < right:
            a = numbers[left]
            b = numbers[right]

            summ = a + b
            
            if summ == target:
                return [left + 1,right + 1]
            
            elif summ > target:
                right -= 1
            
            else:
                left += 1
