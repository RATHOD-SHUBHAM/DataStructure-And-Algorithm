
def staircaseTraversal(height, maxSteps):
    cur_step = 0
    dic = {}
    return bottomUp(cur_step, dic, height, maxSteps)


def  bottomUp(cur_step, dic, height, maxSteps):
    # base case
    if cur_step == height:
        return 1

    if cur_step > height:
        return 0

    if cur_step in dic:
        return dic[cur_step]

    count = 0
    for step in range(1, maxSteps + 1):
        count += bottomUp(cur_step + step, dic, height, maxSteps)
    dic[cur_step] = count

    return dic[cur_step]
