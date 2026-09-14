class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Brute force

        n = len(nums)
        q = collections.deque()

        for i in range(k):
            q.append(nums[i])
        
        max_output = []
        max_output.append(max(q)) 

        for i in range(k, n):
            q.popleft()
            q.append(nums[i])

            # max(q) scans all k elements of the deque every single time, from scratch. You call this once per window, and there are roughly n - k + 1 windows — so total work is O(n * k)
            max_output.append(max(q))
        
        return max_output



# =========================   =========================     =========================   ==================

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = collections.deque()  # stores INDICES, values decreasing left to right
        result = []

        for i, num in enumerate(nums):
            # Check if index is safe: Remove indices that fall outside the window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Maintain decreasing order: pop smaller values from the back,
            # since they can never be the max while num is still in the window
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(i)

            # We only want to record a "max" answer once the window has actually reached its full size, k. Before that, the window is still filling up for the first time and isn't a valid k-sized window yet.
            if i >= k - 1:
                result.append(nums[dq[0]])  # front is always the current max

        return result