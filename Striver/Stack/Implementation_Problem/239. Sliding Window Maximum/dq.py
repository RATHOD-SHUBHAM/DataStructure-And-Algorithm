# Tc and Sc: O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        op = []

        dq = collections.deque()

        for i in range(n):
            # Pop element that are not part of current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            cur_ele = nums[i]
            
            # Check if the current element is the max elemenet, Pop from top of stack
            while dq and cur_ele > nums[dq[-1]]:
                dq.pop()
            
            dq.append(i) # Monotonic deque

            # Start appending only after we reach the window size
            if i >= k - 1:
                op.append(nums[dq[0]])

        return op
            
