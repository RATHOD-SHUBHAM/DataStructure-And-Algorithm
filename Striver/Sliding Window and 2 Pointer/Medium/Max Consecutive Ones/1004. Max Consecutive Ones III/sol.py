class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        stack = []

        left = right = 0

        max_len = 0

        while right < n:
            cur_num = nums[right]

            if cur_num == 0:
                
                if len(stack) < k:
                    # Expand the current window
                    stack.append(right)
                
                else:
                    # Move the window
                    if k != 0:
                        cur_len = right - left
                        max_len = max(max_len , cur_len)

                        left = stack.pop(0) + 1
                        stack.append(right)
                    else:
                        cur_len = right - left
                        max_len = max(max_len , cur_len)
                        left = right + 1
            
            right += 1
        
        cur_len = right - left
        max_len = max(max_len , cur_len)

        return max_len
    

# ----------  Same Solution modified code  ------------------


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        stack = []

        left = right = 0

        max_len = 0

        while right < n:
            cur_num = nums[right]

            if cur_num == 0:
                
                if len(stack) < k:
                    # Expand the current window
                    stack.append(right)
                
                else:
                    cur_len = right - left
                    max_len = max(max_len , cur_len)

                    # Move the window
                    if k != 0:
                        left = stack.pop(0) + 1
                        stack.append(right)
                    else:
                        left = right + 1
            
            right += 1
        
        cur_len = right - left
        max_len = max(max_len , cur_len)

        return max_len