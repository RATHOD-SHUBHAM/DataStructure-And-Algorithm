# Tc: O(n + q) where n = length of nums, q = number of queries
# Sc: O(n), where n = length of nums

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        # Step 1: Preprocessing Phase: Build a map of where each number appears
        # get the kth occurnaces og number
        dic = collections.defaultdict(list)

        n = len(nums)

        for idx in range(n):
            dic[nums[idx]].append(idx)

        # Step 2: Query Phase: For each query k, lookup the kth position directly
        # Capture the Kth occurance of x
        m = len(dic[x])

        op = []

        for i in range(len(queries)):
            k_th_occurance = queries[i]

            # The boundary check if k_th occurance of x exist or not
            if k_th_occurance > m:
                op.append(-1)
            else:
                op.append(dic[x][k_th_occurance - 1])
        
        return op
    

# -------------------------- Using List ----------------------------

# Tc: O(n + q) where n = length of nums, q = number of queries
# Sc: O(n), where n = length of nums

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        # Step 1: Preprocessing Phase: Build a map of where each number appears
        # get the kth occurnaces og number
        occurances = []

        n = len(nums)

        for idx in range(n):
            if nums[idx] == x:
                occurances.append(idx)

        # Step 2: Query Phase: For each query k, lookup the kth position directly
        # Capture the Kth occurance of x
        m = len(occurances)

        op = []

        for i in range(len(queries)):
            k_th_occurance = queries[i]

            # The boundary check if k_th occurance of x exist or not
            if k_th_occurance > m:
                op.append(-1)
            else:
                op.append(occurances[k_th_occurance - 1])
        
        return op
