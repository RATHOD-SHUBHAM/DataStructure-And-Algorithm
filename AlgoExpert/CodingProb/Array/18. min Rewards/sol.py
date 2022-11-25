# Tc and Sc = O(n)

def minRewards(scores):
    n = len(scores)
    reward = [1] * n

    # checking the left side and assigning the reward
    for i in range(1, n):
        if scores[i] > scores[i-1]:
            reward[i] = 1 + reward[i - 1]

    # checking the right side and assigning the reward
    for i in reversed(range(n - 1)):
        if scores[i] > scores[i+1]:
            reward[i] = max(reward[i] , reward[i+1] + 1)

    return sum(reward)
        
