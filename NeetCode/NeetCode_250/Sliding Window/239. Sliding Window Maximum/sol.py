class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Brute force

        # n = len(nums)
        # q = collections.deque()

        # for i in range(k):
        #     q.append(nums[i])
        
        # max_output = []
        # max_output.append(max(q)) 

        # for i in range(k, n):
        #     q.popleft()
        #     q.append(nums[i])

        #     # max(q) scans all k elements of the deque every single time, from scratch. You call this once per window, and there are roughly n - k + 1 windows — so total work is O(n * k)
        #     max_output.append(max(q))
        
        # return max_output

        """
        Idea for optimization:
        
        - With n = 10^5 and k potentially also up to 10^5, worst case n * k = 10^{10} operations. That's the TLE — using a deque for the window doesn't help if you still brute-force the max over it every time. The deque here is just storing raw values; it's not actually doing anything smarter than a plain array with two pointers would.

        - Your solution is O(n*k), which in the worst case (k close to n) becomes O(n^2) ≈ 10^{10} — a dead giveaway this is too slow. The presence of two size parameters (n and k) where k can be as large as n is itself a red flag: any solution whose complexity multiplies them together is suspect unless one of them is guaranteed small.

        - The fix: avoid recomputing max — maintain it incrementally

        You need a structure where, as the window slides, you can get the max in O(1) amortized, without rescanning. The classic tool for this is a monotonic deque — not just a deque of raw values, but one that maintains a special invariant: it always keeps its elements in decreasing order, so the front is always the current max.

        - Logic
        We store indices in the order we see them (no sorting), but before adding a new one, we remove everything at the back that's smaller than the new value — so that the front of the deque is always guaranteed to be the greatest value currently valid in the window.

        That single invariant (front = current max) is what gives us O(1) max lookup every step, and combined with evicting expired indices from the front, the whole thing runs in O(n) total.
        """

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