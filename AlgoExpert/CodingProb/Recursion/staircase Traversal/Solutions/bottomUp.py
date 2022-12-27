def staircaseTraversal(height, maxSteps):
    cur_step = 0
    return bottomUp(cur_step, height, maxSteps)

def  bottomUp(cur_step, height, maxSteps):
    # base case
    if cur_step == height:
        return 1

    if cur_step > height:
        return 0

    count = 0
    for step in range(1, maxSteps + 1):
        count += bottomUp(cur_step + step, height, maxSteps)

    return count
