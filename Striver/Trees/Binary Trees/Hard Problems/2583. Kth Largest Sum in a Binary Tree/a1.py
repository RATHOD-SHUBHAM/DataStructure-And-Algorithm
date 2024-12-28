# ------------------------------ Sort ------------------------------

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

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

        sum_of_level.sort()

        return sum_of_level[-k]


# ------------------------------ Heap ------------------------------

import heapq

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findKthLargest(self, nums, k):
        n = len(nums)
        
        heapq.heapify(nums)

        k_largest = -1
        for _ in range(k):
            k_largest = heapq.heappop(nums)
        
        return k_largest


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
            
            sum_of_level.append(-1 * cur_sum)
        
        # print(sum_of_level)

        if len(sum_of_level) < k:
            return -1

        # Using Heqp
        kth_largest = self.findKthLargest(sum_of_level, k)

        # Convert back to positive number
        return -1 * kth_largest
    

# ------------------------------ Count Sort ------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countSort(self, arr):
        n = len(arr)
        m = max(arr)

        count_array = [0] * (m + 1)
        sorted_array = [0] * n

        # Step 1: get the frequency of array
        for i in range(n):
            idx = arr[i]
            count_array[idx] += 1
        
        # Step 2: Prefix Sum
        for i in range(1, m+1):
            count_array[i] += count_array[i - 1]
        
        # Step 3: Sort the array
        for i in reversed(range(n)):
            countIdx = arr[i]
            sortedIdx = count_array[countIdx] - 1

            count_array[countIdx] -= 1

            sorted_array[sortedIdx] = arr[i]
        
        return sorted_array

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        level_sum = []

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
            
            level_sum.append(cur_sum)
        
        # print(level_sum)

        if len(level_sum) < k:
            return -1
        
        sorted_array = self.countSort(level_sum)
        # print(sorted_array)
        return sorted_array[-k]



# ------------------------------ Quick Select ------------------------------

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