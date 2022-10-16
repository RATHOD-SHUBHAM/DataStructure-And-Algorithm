# Exact copy of  question : 31 Next Permutation
# Tc: O(n)
# Sc: O(1)


class Solution:
    def swap(self, i , j , nums):
        nums[i], nums[j] = nums[j], nums[i]
        
    def reverse(self, left , right, nums):
        while left < right:
            self.swap(left, right, nums)
            left += 1
            right -= 1
        return nums
    
    
    def nextGreaterElement(self, n: int) -> int:
        maxvalue_of_32_bit_integer = math.pow(2,31) - 1
        
        
        if 1 <= n <= 9 :
            return -1
        
        # converting to list
        nums = [int(x) for x in str(n)]
        print(nums)
        
        n = len(nums)
        
        # step 1: find the division point
        div_point = n - 2
        
        while div_point >= 0 and nums[div_point] >=  nums[div_point + 1]:
            div_point -= 1
            
        # step 2: swap element
        if div_point < 0:
            # self.reverse(0, n-1, nums)
            return -1
        else:
            for i in reversed(range(div_point + 1 , n)):
                if nums[div_point] < nums[i]:
                    self.swap(div_point , i , nums)
                    break
            
            self.reverse(div_point + 1, n - 1, nums)
            
        num = [str(x) for x in nums]
        nums = "".join(num)
        # print(nums)
        return int(nums) if maxvalue_of_32_bit_integer >= int(nums) else -1