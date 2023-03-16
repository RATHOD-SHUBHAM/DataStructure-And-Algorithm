# logic here is to check if i can choose a more minimum value than the current element present
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left = min(nums)
        right = max(nums)
        
        while left < right:
            # print("left : ", left)
            # print("right : ", right)
            mid = left + (right - left) // 2
            # print("mid : ", mid)
            
            # pointer to skip adjacent element
            skip = False
            
            # pointer to check of k houses were choosen
            taken = 0
            
            for house in nums:
                if skip:
                    # flip the pointer
                    skip = False
                    continue
                
                # if the current house value is less than mid value
                if house <= mid:
                    taken += 1
                    skip = True
                    
            # if minimum number of value is taken
            if taken >= k:
                right = mid
            else:
                left = mid + 1
                
            # print("\n")
                
                
        return left