'''
a + b + c + d = value
a + b = x

x + c + d = value -> threeSum

'''

# Tc: O(n^3) | O(n)

def fourNumberSum(array, targetSum):
    array.sort()
    op = []
    n = len(array)

    for i in range(n):
        a = array[i]
        for j in range(i+1 , n):
            b = array[j]

            x = a + b
            left = j + 1
            right = n - 1

            while left < right:
                c = array[left]
                d = array[right]
                
                curSum = x + c + d

                if curSum == targetSum:
                    four_sum = [a, b, c, d]
                    op.append(four_sum)
                    left += 1
                    right -= 1
                elif curSum > targetSum:
                    right -= 1
                else:
                    left += 1

    return op