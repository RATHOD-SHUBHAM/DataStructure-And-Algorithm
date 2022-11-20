# k - sum - Universal

# Tc: O(n^3) | O(n)

def fourNumberSum(array, targetSum):
    array.sort()
    k = 4
    return k_sum(array , targetSum , k)
    
def k_sum(nums, target , k):
    res = []
    
    # base case
    if not nums:
        return res
    
    # this step is not compulsory. but will make the process fast
    avg_sum = target // k
    
    if avg_sum < nums[0] or avg_sum > nums[-1]:
        return res
    # until here ----------------------------------------------------
    
    if k == 2:
        return two_sum(nums, target)
    
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            for pair in k_sum(nums[i+1 : ], target - nums[i], k - 1):
                res.append( [nums[i]] + pair)
                
    return res

def two_sum(nums, target):
    pair = []
    cache = {}
    
    for i in range(len(nums)):
        diff = target - nums[i]
        
        if len(pair) == 0 or nums[i] != pair[-1][1]:
            if diff in cache:
                pair.append([diff, nums[i]])
                
        cache[nums[i]] = i
    
    return pair