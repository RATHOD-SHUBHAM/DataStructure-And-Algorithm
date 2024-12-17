# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        k = n - k

        startIdx = 0
        endIdx = n -1

        return self.quickSelect(startIdx, endIdx, nums, k, n)
    
    def quickSelect(self, startIdx, endIdx, nums, k, n):
        if startIdx > endIdx:
            return
        
        pivot = startIdx
        left = startIdx + 1
        right = endIdx

        while left <= right:
            
            if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
                self.swap(left, right, nums)
            
            if nums[left] <= nums[pivot]:
                left += 1
            
            if nums[right] >= nums[pivot]:
                right -= 1
        
        self.swap(pivot, right, nums)

        if right == k:
            return nums[right]
        elif right < k:
            startIdx = right + 1
            return self.quickSelect(startIdx, endIdx, nums, k, n)
        else:
            endIdx = right - 1
            return self.quickSelect(startIdx, endIdx, nums, k, n)

    def swap(self, i , j , nums):
        nums[i] , nums[j] = nums[j] , nums[i]

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sum_of_level = []

        queue = [root]

        while queue:
            q_len = len(queue)
            cur_sum = 0

            for _ in range(q_len):
                node = queue.pop(0)

                cur_sum += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            sum_of_level.append(cur_sum)
        
        # print(sum_of_level)

        if len(sum_of_level) < k:
            return -1

        # Quick Select Algorithm
        kth_largest = self.findKthLargest(sum_of_level, k)

        return kth_largest