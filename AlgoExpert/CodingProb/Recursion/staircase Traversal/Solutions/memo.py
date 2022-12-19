def staircaseTraversal(height, maxSteps):
    memo = {
        0 : 1
    }

    return helper(height, maxSteps, memo)
    
def helper(height, maxSteps, memo):
    if height < 0:
        return 0
        
    if height in memo:
        return memo[height]
    
    count = 0
    # go through every combination of step
    for i in range(1, maxSteps + 1):
        new_height = height - i
        count += helper(new_height, maxSteps, memo)
    memo[height] = count
    
    return memo[height]
    
        
