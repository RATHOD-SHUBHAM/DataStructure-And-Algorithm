class Solution:
    def get_floor(self, nums, n, target):
        '''Duplicate: Return the rightmost index of target'''
        ans = -1
        
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] <= target:
                if nums[mid] == target:
                    ans = mid
                left = mid + 1 #Check if there is even more Larger number
            else:
                right = mid - 1
        
        return ans

    def get_ceil(self, nums, n, target):
        '''Duplicate: Return the leftmsot index of target'''
        ans = n
        
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] >= target:
                if nums[mid] == target:
                    ans = mid
                
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
        

    def count(self,arr, n, x):
        # code here
        end = self.get_floor(arr, n, x)
        start = self.get_ceil(arr, n, x)
        
        if start == n:
            return 0
        elif end == -1:
            return 0
        else:
            return end - start + 1