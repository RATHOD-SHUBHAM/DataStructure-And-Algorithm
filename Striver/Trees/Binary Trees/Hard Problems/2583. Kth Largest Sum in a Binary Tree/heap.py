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
        