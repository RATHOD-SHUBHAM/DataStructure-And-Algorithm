# Brute Nested

class Solution:
    def __init__(self):
        self.result = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backTrack(i, nums):
            if len(st) == k:
                self.result.append(st.copy())
                return
            
            if i >= n:
                return

            
            st.append(nums[i])
            backTrack(i + 1, nums)

            st.pop()
            backTrack(i + 1, nums)

            return
        
        st = []
        nums = [None] * n

        for i in range(n):
            nums[i] = i + 1
        
        backTrack(0, nums)
        
        return self.result

# ------------------------------------------------------------------------------

# Brute Local function
    
class Solution:
    def __init__(self):
        self.result = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
 
        
        st = []
        i = 0
        self.backTrack(i, st, nums, n, k)

        return self.result
    
    def backTrack(self, i, st, nums, n, k):
        # base case
        if len(st) == k:
            self.result.append(st[::])
            return
        
        if i >= n:
            return
        
        # Include the current number
        st.append(nums[i])
        self.backTrack(i + 1, st, nums, n, k)

        # Remove the current number
        st.pop()
        self.backTrack(i + 1, st, nums, n, k)

        return
    
# ------------------------------------------------------------------------------
# Optimized Nested Function

class Solution:
    def __init__(self):
        self.result = []
        self.st = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backTrack(start):
            # base case
            if len(self.st) == k:
                self.result.append(self.st.copy())
                return
            
            for i in range(start, n + 1):
                self.st.append(i)
                backTrack(i + 1)
                self.st.pop()
            
            return
        
        start = 1
        backTrack(start)

        return self.result


# ------------------------------------------------------------------------------
# Optimized local Function     
    
class Solution:
    def __init__(self):
        self.result = []
        self.st = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        start = 1
        self.backTrack(start, n, k)

        return self.result
    
    def backTrack(self, start, n , k):
        # base case
        if len(self.st) == k:
            self.result.append(self.st.copy())
            return
        
        # Move across and add each element
        for i in range(start, n+1):
            self.st.append(i)
            self.backTrack(i + 1, n, k)
            self.st.pop()
        
        return