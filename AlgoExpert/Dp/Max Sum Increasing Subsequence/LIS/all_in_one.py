# --------------------------------- Recursion ------------------------------------------------------------------

# Tc: O(2^n) | Sc: O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        curIdx = 0
        prevIdx = -1 # we need to keep track of prev value as we need to increasing sub sequence
        
        return self.LIS(curIdx, prevIdx, nums)
    
    def LIS(self, curIdx, prevIdx, nums):
        # base case
        if curIdx >= len(nums):
            return 0
        
        max_len = 0
        
        # code
        dontTake = 0 + self.LIS( curIdx + 1, prevIdx , nums)
        max_len += dontTake
        
        if prevIdx == -1 or nums[curIdx] > nums[prevIdx]:
            take = 1 + self.LIS( curIdx + 1, curIdx, nums)
            max_len = max(max_len , take)
            
        return max_len

# --------------------------------- dp ------------------------------------------------------------------

# TC: O(n)^2 | Sc: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [1, 2, 3, 4]
        n = len(nums)
        dp = [1] * n
        
        
        for curIdx in range(1, n):
            for prevIdx in range(curIdx):
                dontTake = 0 + dp[curIdx]
                dp[curIdx] = dontTake
                
                # the value has to be strictly increasing
                if nums[prevIdx] < nums[curIdx]:
                    take =  1 + dp[prevIdx]
                    dp[curIdx] = max(dp[curIdx] , take)
                    
                
                
                    
        return max(dp)

# --------------------------------- dp with subsequence ------------------------------------------------------------------

# Tc: O(n^2) | Sc: O(n) 
def maxSumIncreasingSubsequence(array):
    n = len(array)

    dp = [num for num in array]

    pointerToSubsequence = [None] * n 

    # here we just dont need longest increasing subsequence, we need max sum longest increasing subsequence
    for curIdx in range(1 , n):
        for prevIdx in range(curIdx):
            if array[prevIdx] < array[curIdx] and  array[curIdx] + dp[prevIdx] > dp[curIdx]:
                dp[curIdx] = array[curIdx] + dp[prevIdx]
                pointerToSubsequence[curIdx] = prevIdx

    print("dp: ", dp)
    maxIndex = dp.index(max(dp))
    return buildSubsequence(array, pointerToSubsequence, maxIndex)

# build using the hash pointer
def buildSubsequence(array, pointerToSubsequence, curIndex):
    subseq = []
    total = 0

    while curIndex is not None:
        total += array[curIndex]
        subseq.append(array[curIndex])
        curIndex = pointerToSubsequence[curIndex]

    return (total, subseq[::-1])
        

# --------------------------------- Binary Search ------------------------------------------------------------------

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize the result
        res = []

        # Binary search to find the index of the smallest number in result that is greater than or equal to the target
        def binarySearch(l, r, target):

            nonlocal res

            # If the left and right pointers meet, we have found the smallest number that is greater than the target
            if l == r:
                return l

            # Find the mid pointer
            m = (r - l) // 2 + l
            # print("mid: ", m)

            # If the number at the mid pointer is equal to the target, we have found a number that is equal to the target
            if res[m] == target:
                return m

            # Else if the number at the mid poitner is less than the target, we search the right side
            elif res[m] < target:
                return binarySearch(m + 1, r, target)

            # Else, we search the left side including the number at mid pointer because it is one of the possible solution since it is greater than the target
            else:
                return binarySearch(l, m, target)

        # Iterate through all numbers
        for n in nums:

            # If the last number in the result is less than the current number
            if not res or res[-1] < n:

                # Append the current number to the result
                res.append(n)

                continue

            # Else, find the index of the smallest number in the result that is greater than or equal to the current number
            # print("res: ", res)
            i = binarySearch(0, len(res) - 1, n)
            # print("index to append: ", i)

            # Replace the current number at such index
            res[i] = n

        return len(res)
    
# --------------------------------- Binary Search ------------------------------------------------------------------
