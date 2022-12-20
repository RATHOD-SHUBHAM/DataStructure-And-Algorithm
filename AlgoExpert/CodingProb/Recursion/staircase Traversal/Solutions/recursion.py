def staircaseTraversal(height, maxSteps):
    # base case
    if height < 0:
        return 0

    if height == 0:
        return 1

    count = 0
    for step in range(1, maxSteps + 1):
        count += staircaseTraversal(height - step, maxSteps)

    return count