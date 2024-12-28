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

        