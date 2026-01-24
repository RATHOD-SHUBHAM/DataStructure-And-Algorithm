# O(n) | O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        left = 0
        right = n - 1

        while left < right:
            cur_sum = numbers[left] + numbers[right]

            if cur_sum == target:
                return [left + 1, right + 1]
            
            elif cur_sum < target:
                left += 1

                # handle duplicate -  [ This is same as comparing individual elements, hence does not change time complexity but is just good at checking duplicates]
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
            
            else:
                right -= 1

                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1