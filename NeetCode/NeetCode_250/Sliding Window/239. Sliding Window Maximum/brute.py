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

        